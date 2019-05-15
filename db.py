from collections import defaultdict
from block import Block
import pickle

class Bucket(object):
	""" Represent a bucket for a blockchain

	Database Structure:
	{
		Bucket_key_0: [...]
		Bucket_key_1: [...]
		...
		Bucket_key_n: [...]
	}

	Args:
		db_file			string
		bucket_key		string

	Attributes:
		_db_file		string
		_bucket_key		string
		_bucket			dict

	"""
	def __init__(self, db_file, bucket_key):
		self._db_file = db_file
		try:
			with open(self._db_file, 'rb') as f:
				self._db = pickle.load(f)
		except FileNotFoundError:
			self._db = defaultdict(list)

		self._bucket_key = bucket_key
		self._bucket = self._db[bucket_key]
		if not self._bucket:
			self._bucket.append(Block())
		
		del self._db

	def __repr__(self):
		return 'Bucket({0!r})'.format(self._bucket)

	def __str__(self):
		return 'Bucket({0!r})'.format(self._bucket)

	def __getitem__(self, index):
		return self._bucket[index]

	def __setitem__(self, index, value):
		self._bucket[index] = value

	def __delitem__(self, index):
		del self._bucket[index]
	
	def __contains__(self, value):
		return value in self._bucket

	def __iter__(self):
		return iter(self._bucket)

	def __len__(self):
		return len(self._bucket)

	def append(self, block):
		return self._bucket.append(block)

	def commit(self):
		try:
			with open(self._db_file, 'rb') as f:
				self._db = pickle.load(f)
		except FileNotFoundError:
			self._db = defaultdict(list)

		with open(self._db_file, 'wb') as f:
			self._db[self._bucket_key] = self._bucket
			pickle.dump(self._db, f)

		del self._db	
	
	def reset(self):
		self._bucket = []

