
import copy
from random import shuffle
from collections import Counter


from Game.Player import Player
from Game.Context import Context, PlayerContext
from Game.Const import Const



class IslandStats:

	def __init__(self):
		self.VICTORIES = 0
		self.NOWINNERS = 0
		self.GAMEOVERS = []

	def add(self, other):
		self.VICTORIES += other.VICTORIES
		self.NOWINNERS += other.NOWINNERS
		self.GAMEOVERS += other.GAMEOVERS

	def describe(self):

		avg = sum(self.GAMEOVERS) / len(self.GAMEOVERS)
		sigma2 = 0
		for i in self.GAMEOVERS:
			sigma2 +=  (i-avg) ** 2
		sigma2 /= len(self.GAMEOVERS)	
		sigma = sigma2 ** 0.5

		return ("" +
				"    VICTORIES = {}\n" +
				"    NOWINNERS = {}\n" +
				"    GAMEOVERS = {}\n" +
				"    GAMEOVERS avg = {:.2f}\n" +
				"    GAMEOVERS sig = {:.2f}\n" +
				"").format(
					self.VICTORIES,
					self.NOWINNERS,
					len(self.GAMEOVERS),
					avg,
					sigma
				)