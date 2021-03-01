import neopixel as np
import board

import options as op
import time

pixels = np.NeoPixel(board.D18, 12)
pixels.fill((0,0,0))

class light_house():
	def __init__(self):
		self.lights = [0] * op.BOT_NUM
		self.curr = [0,0,0]
		self.count = 0
		self.state = 0
		self.start = 0

	def ready(self):
		READY_COLOR = [0, 255, 255]
		while(self.curr != READY_COLOR):
			fade(self.curr, READY_COLOR)

	def turn_on(self, message):
		for n in range(4):
			if(message == op.WORD_LIST[n]):
				self.lights[n] = 1
				self.start = time.time()
				break

	def main(self):
		if(self.lights[self.state]):
			if(self.curr != op.LIGHT_HOUSE[op.WORD_LIST[self.state]]):
				fade(self.curr, op.LIGHT_HOUSE[op.WORD_LIST[self.state]])
			else:
				self.state = (self.state + 1) % op.BOT_NUM
		else:
			self.state = (self.state + 1) % op.BOT_NUM

		if(self.start + (op.DURATION * 3600) <= time.time()):
			self.lights[:op.BOT_NUM] = [0] * op.BOT_NUM
			fade(self.curr, [0,0,0])

def fade(curr, goto):
	for n in range(3):
		if(goto[n] != curr[n]):
			curr[n] += 1 if goto[n] > curr[n] else -1
	pixels.fill(curr)
