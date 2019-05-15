from block import Block
from db import Bucket


DB_FILE = 'blockchain.db'
BLOCK_BUCKET = 'blocks'


class Blockchain(object):
	""" Represents a sequence of blocks

	Args:
		None

	Attributes:
		None

	"""
	def __init__(self):
		self._blocks = Bucket(DB_FILE, BLOCK_BUCKET)

	def __repr__(self):
		return 'Blockchain({0!r})'.format(self._blocks)

	def __str__(self):
		self._blocks.commit()
		return 'Blockchain({0!r})'.format(self._blocks)

	def addBlock(self, transaction):
		prevBlock = self._blocks[len(self._blocks)-1]
		self._blocks.append( Block(prevBlock.height, prevBlock.hash, transaction) )
		self._blocks.commit()

	def printBlock(self, height):
		block = self._blocks[height]
		print(block)
		self._blocks.commit()
