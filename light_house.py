import neopixel as np
import board

import options as op
import time

class light_house():
	def __init__(self):
		self.lights = [0] * op.BOT_NUM
		self.curr = [0,0,0]
		self.count = 0
		self.state = 0
		self.start = 0

    self.pixels = np.NeoPixel(board.D18, 12)
    self.pixels.fill((0, 0, 0))

	def ready(self):
		READY_COLOR = [144, 238, 144]
    self.fade(READY_COLOR)

	def turn_on(self, message):
		for n in range(4):
			if(message == op.WORD_LIST[n]):
				self.lights[n] = 1
				self.start = time.time()
				break

  def fade(self, goto):
    while(self.curr != goto):
      for n in range(3):
        if(goto[n] != self.curr[n]):
          self.curr[n] += 1 if goto[n] > self.curr[n] else -1

      self.pixels.fill(curr)

  def clear(self):
    self.fade((0,0,0))

	def main(self):
		if(self.lights[self.state]):
      self.fade(op.LIGHT_HOUSE[op.WORD_LIST[self.state]])
		  self.state = (self.state + 1) % op.BOT_NUM
      self.clear()
		else:
			self.state = (self.state + 1) % op.BOT_NUM

		if(self.start + (op.DURATION * 3600) <= time.time()):
			self.lights[:op.BOT_NUM] = [0] * op.BOT_NUM
			self.clear()
