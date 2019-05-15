import argparse
from blockchain import Blockchain

def parse():
	parser = argparse.ArgumentParser(description='Blockchain hw1')

	parser.add_argument('--printchain', action='store_true')

	subparsers = parser.add_subparsers(help='commmand')

	addblock_parser = subparsers.add_parser('addblock', help='Add a block to the chain')
	addblock_parser.add_argument('--transaction', type=str, default='', help='Block transaction')

	printchain_parser = subparsers.add_parser('printblock', help='Print a specific block by height')
	printchain_parser.add_argument('--height', type=int, default=0, dest='block_height', help='Height of the block')

	args = parser.parse_args()
	return args


def print_chain():
	print(Blockchain())


def add_block(transaction):
	blockchain = Blockchain()
	blockchain.addBlock(transaction)

def print_block(height):
	blockchain = Blockchain()
	blockchain.printBlock(height)


if __name__ == '__main__':
	args = parse()

	if args.printchain:
		print_chain()

	if hasattr(args, 'transaction'):
		add_block(args.transaction)

	if hasattr(args, 'block_height'):
		print_block(args.block_height)
		
