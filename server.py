import time, json
from flask import Flask, jsonify
from modules.blockchain import Blockchain, Block

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine_block', methods= ['GET'])
def mine_block():
    pre_block = blockchain.get_latest_block()
    pre_proof = pre_block.proof
    proof = blockchain.proof_of_work(pre_proof)
    new_block = Block(pre_block.index+1, time.time(), {}, proof, pre_block.hash)
    new_block = blockchain.add_block(new_block)
    response = {
        'message': 'Congrats, block created',
        'block': json.dumps(new_block, default= lambda x: x.__dict__),
    }
    return jsonify(response), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': json.dumps(blockchain.chain, default= lambda x: x.__dict__),
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


app.run('0.0.0.0', 5000)