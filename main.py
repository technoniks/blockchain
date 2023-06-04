import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), 'Genesis Block', '0')

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Usage example
blockchain = Blockchain()

block1 = Block(1, time.time(), {'amount': 100}, '')
block2 = Block(2, time.time(), {'amount': 50}, '')
block3 = Block(3, time.time(), {'amount': 200}, '')

blockchain.add_block(block1)
blockchain.add_block(block2)
blockchain.add_block(block3)

print('Blockchain is valid:', blockchain.is_chain_valid())

# Tampering with the chain
block2.data = {'amount': 300}
block2.hash = block2.calculate_hash()

print('Blockchain is valid after tampering:', blockchain.is_chain_valid())