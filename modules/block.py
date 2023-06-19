import hashlib, json
from json import JSONEncoder

class Block:
    def __init__(self, index, timestamp, data, proof, previous_hash = ''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.proof = proof
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()
