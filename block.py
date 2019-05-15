import time
from pow import ProofOfWork

BITS = 20

class Block(object):
	""" Represents a new Block object

	Args:
		prevHeight			int
		prev_block_hash		[]byte
		transactions		string

	Attributes:
		_height				int
		_prev_block_hash	[]byte
		_time				int
		_bits				int
		_nonce				int
		_transactions		[]byte
		_hash				[]byte

	"""
	def __init__(self, prevHeight=-1, prev_block_hash=bytes('', 'utf-8'), transactions='Welcome to blockchain'):
		self._height = prevHeight + 1
		self._prev_block_hash = prev_block_hash
		self._time = int(time.time())
		self._bits = BITS
		self._nonce = None
		self._transactions = transactions.encode('utf-8')
		self._hash = None
		self.setHash()
	
	def __repr__(self):
		return 'Block(height={0!r}, prev_block_hash={1!r}, time={2!r}, bits={3!r}, nonce={4!r},  tx={5!r}, hash={6!r})'.format(
			self._height, self._prev_block_hash, self._time, self._bits, self._nonce, self._transactions, self._hash)

	def __str__(self):
		return 'Block(height={0!r}, prev_block_hash={1!r}, time={2!r}, bits={3!r}, nonce={4!r},  tx={5!r}, hash={6!r})'.format(
			self._height, self._prev_block_hash, self._time, self._bits, self._nonce, self._transactions, self._hash)

	@property
	def height(self):
		return self._height

	@property
	def prev_block_hash(self):
		return self._prev_block_hash

	@property
	def time(self):
		return self._time

	@property
	def bits(self):
		return self._bits

	@property
	def nonce(self):
		return self._nonce

	@property
	def transactions(self):
		return self._transactions

	@property
	def hash(self):
		return self._hash
	
	def setHash(self):
		pow = ProofOfWork(self)
		nonce, hash = pow.run()

		self._nonce = nonce
		self._hash = hash
