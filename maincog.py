import discord
from discord.ext import tasks, commands

import digitalio
import board
import time

import ident
import options as op
import light_house as lh

class MainCog(commands.Cog):  
	def __init__(self, bot):
		self.bot = bot
		self.channel = None
		self.lh = lh.light_house()

		self.button = digitalio.DigitalInOut(board.D17)
		self.button.direction = digitalio.Direction.INPUT
		self.button.pull = digitalio.Pull.UP

	def cog_unload(self):
		self.button.cancel()

	@commands.Cog.listener()
	async def on_ready(self):
		while(self.channel == None):
			self.channel = self.bot.get_channel(op.CHANNEL)
			time.sleep(3)

		self.lh.ready()		

		if(not self.main.is_running()):
			self.main.start()
		print('Signed In: ' + str(self.channel))

	@commands.Cog.listener()
	async def on_message(self, message):
		for word in op.WORD_LIST:
			if message.content.startswith(word):
				self.lh.turn_on(word)

	@tasks.loop(seconds=0.1)
	async def main(self):
		if(not self.button.value and not self.lh.lights[ident.ID]):
			await self.channel.send(op.WORD_LIST[ident.ID])
		self.lh.main()

def setup(bot):
    bot.add_cog(MainCog(bot))
