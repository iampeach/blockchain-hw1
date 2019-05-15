from block import Block
from blockchain import Blockchain
from db import Bucket

if __name__ == "__main__":
#	blockchain = Blockchain()
#	print(blockchain)
#	blockchain.addBlock('addBlock')
#	print(blockchain)
	bucket = Bucket('test.db', 'block')
	bucket2 = Bucket('test.db', 'block2')
	bucket['key1'] = 'value'
	print(bucket['key'])
	bucket2['key2'] = 'value'
	bucket.commit()
	bucket2.commit()
	print(bucket)
	print(bucket2)
