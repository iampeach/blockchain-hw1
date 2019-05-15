import hashlib
import sys

MAX_NONCE = sys.maxsize #INT_MAX

class ProofOfWork(object):
	""" Performs a power-of-work
	
	Args:
		block		Block
	
	Attributes:
		_block		Block
		_target		int

	"""
	def __init__(self, block):
		self._block = block
		self._target = 1 << ( 256 - block.bits )

	def _prepare_data(self, nonce):
		# data_list = str(self._block)
		data_list = [ self._block.prev_block_hash.decode('utf-8'),
					  self._block.transactions.decode('utf-8'),
					  str(self._block.time),
					  str(self._block.bits),
					  str(nonce) ]

		# return []byte(self._block)
		return ''.join(data_list).encode('utf-8')

	def run(self):
		print ('Start mining a new block')
		nonce = 0
		while nonce < MAX_NONCE:
			data = self._prepare_data(nonce)
			hash_hex = hashlib.sha256(data).hexdigest()
			print('%s \r' % (hash_hex))
			hash_int = int(hash_hex, 16)

			if hash_int < self._target:
				break
			else:
				nonce += 1	

		print ('\n\n')
		print ('End mining')

		return nonce, hash_hex.encode('utf-8')

	def validate(self):
		data = self._prepare_data(self._block.nonce)
		hash_hex = hashlib.sha256(data).hexdigest() 
		hash_int = int(hash_hex, 16)

		return True if hash_int < self._target else False
