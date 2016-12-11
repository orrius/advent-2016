import operator
from collections import namedtuple

from enum import Enum

paths = ['L5', 'R1', 'R3', 'L4', 'R3', 'R1', 'L3', 'L2', 'R3', 'L5', 'L1', 'L2', 'R5', 'L1', 'R5', 'R1', 'L4', 'R1', 'R3', 'L4', 'L1', 'R2', 'R5', 'R3', 'R1', 'R1', 'L1', 'R1', 'L1', 'L2', 'L1', 'R2', 'L5', 'L188', 'L4', 'R1', 'R4', 'L3', 'R47', 'R1', 'L1', 'R77', 'R5', 'L2', 'R1', 'L2', 'R4', 'L5', 'L1', 'R3', 'R187', 'L4', 'L3', 'L3', 'R2', 'L3', 'L5', 'L4', 'L4', 'R1', 'R5', 'L4', 'L3', 'L3', 'L3', 'L2', 'L5', 'R1', 'L2', 'R5', 'L3', 'L4', 'R4', 'L5', 'R3', 'R4', 'L2', 'L1', 'L4', 'R1', 'L3', 'R1', 'R3', 'L2', 'R1', 'R4', 'R5', 'L3', 'R5', 'R3', 'L3', 'R4', 'L2', 'L5', 'L1', 'L1', 'R3', 'R1', 'L4', 'R3', 'R3', 'L2', 'R5', 'R4', 'R1', 'R3', 'L4', 'R3', 'R3', 'L2', 'L4', 'L5', 'R1', 'L4', 'L5', 'R4', 'L2', 'L1', 'L3', 'L3', 'L5', 'R3', 'L4', 'L3', 'R5', 'R4', 'R2', 'L4', 'R2', 'R3', 'L3', 'R4', 'L1', 'L3', 'R2', 'R1', 'R5', 'L4', 'L5', 'L5', 'R4', 'L5', 'L2', 'L4', 'R4', 'R4', 'R1', 'L3', 'L2', 'L4', 'R3']

Point = namedtuple('Point', ['x', 'y'])

class Direction(Enum):
	north = 1
	east = 2
	south = 3
	west = 4

	def turn_right(self):
		if self.value < 4:
			return Direction(self.value + 1)
		else:
			return Direction(1)

	def turn_left(self):
		if self.value > 1:
			return Direction(self.value - 1)
		else:
			return Direction(4)

class Position():
	def __init__(self, x, y, direction):
		self.x = x
		self.y = y
		self.direction = direction
		self.previous_positions = [(0, 0)]

	def __repr__(self):
		return 'x: {}, y: {}, direction: {}'.format(self.x, self.y, self.direction)

	def turn_right(self):
		self.direction = self.direction.turn_right()

	def turn_left(self):
		self.direction = self.direction.turn_left()

	def move_straight(self, num_of_blocks):
		if self.direction.name == 'north':
			for _ in range(num_of_blocks):
				self.y += 1
				self.previous_positions.append((self.x, self.y))
		if self.direction.name == 'east':
			for _ in range(num_of_blocks):
				self.x += 1
				self.previous_positions.append((self.x, self.y))
		if self.direction.name == 'south':
			for _ in range(num_of_blocks):
				self.y -= 1
				self.previous_positions.append((self.x, self.y))
		if self.direction.name == 'west':
			for _ in range(num_of_blocks):
				self.x -= 1
				self.previous_positions.append((self.x, self.y))

	def move(self, steps):
		"""Calculates & sets new coordinates/direction after movement

		Args:
			steps(str):	Right/left & how many blocks
		Returns:
			Position:	New coordinates
		"""
		direction, length = steps[0], steps[1:]
		length = int(length)
		if direction == 'L':
			self.turn_left()
		elif direction == 'R':
			self.turn_right()
		self.move_straight(length)


pos = Position(0,0, Direction(1))

for path in paths:
    pos.move(path)

print("The shortest distance is: {}".format(abs(pos.x) + abs(pos.y)))

for i in range(len(pos.previous_positions)):
	if pos.previous_positions[i] in pos.previous_positions[i + 1:]:
		print("The shortest distance is: {}".format(abs(pos.previous_positions[i][0]) + abs(pos.previous_positions[i][1])))
		break