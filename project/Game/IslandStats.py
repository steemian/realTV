
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
		self.PointsForTrial = 0
		self.PointsForGO = 0
		self.PointsForVic = 0

	def add(self, other):
		self.VICTORIES += other.VICTORIES
		self.NOWINNERS += other.NOWINNERS
		self.GAMEOVERS += other.GAMEOVERS
		self.PointsForTrial += other.PointsForTrial
		self.PointsForGO += other.PointsForGO
		self.PointsForVic += other.PointsForVic

	def describe(self):

		avg = sum(self.GAMEOVERS) / len(self.GAMEOVERS)
		sigma2 = 0
		for i in self.GAMEOVERS:
			sigma2 +=  (i-avg) ** 2
		sigma2 /= len(self.GAMEOVERS)	
		sigma = sigma2 ** 0.5

		return ("" +
				"    Pts for VICTORY  = {}\n" +				
				"    Pts for GAMEOVER = {}\n" +				
				"    Pts for Trial    = {}\n" +				
				"    -------\n"
				"    VICTORIES = {}\n" +
				"    NOWINNERS = {}\n" +
				"    GAMEOVERS = {}\n" +
				"    GAMEOVERS avg = {:.2f}\n" +
				"    GAMEOVERS sig = {:.2f}\n" +
				"").format(
					self.PointsForVic,
					self.PointsForGO,
					self.PointsForTrial,

					self.VICTORIES,
					self.NOWINNERS,
					len(self.GAMEOVERS),
					avg,
					sigma
				)