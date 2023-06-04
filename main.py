import time
from modules.blockchain import Blockchain
from modules.block import Block

blockchain = Blockchain()

block1 = Block(1, time.time(), {'amount': 100})
block2 = Block(2, time.time(), {'amount': 50})
block3 = Block(3, time.time(), {'amount': 200})

blockchain.add_block(block1)
blockchain.add_block(block2)
blockchain.add_block(block3)

print('Blockchain is valid:', blockchain.is_chain_valid())

# Tampering with the chain
block2.data = {'amount': 300}
block2.hash = block2.calculate_hash()

print('Blockchain is valid after tampering:', blockchain.is_chain_valid())