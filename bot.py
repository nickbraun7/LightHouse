from discord.ext import commands
import ident

bot = commands.Bot(command_prefix='!')

bot.load_extension("maincog")

bot.run(ident.TOKEN)
