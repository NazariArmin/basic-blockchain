from flask import Flask, jsonify, request
from blockchain import Blockchain
from sys import argv


my_block_chain = Blockchain()
app = Flask(__name__)
port = int(argv[1])

@app.route('/chain')
def get_chain():
    res = {
        "chain":my_block_chain.get_chain
    }
    print(res)
    return jsonify(res)

@app.route('/transaction/create', methods=['POST'])
def new_trx():
    values = request.get_json()
    my_block_chain.new_transaction(values['sender'], values['receiver'], values['amount'])
    res = {
        "msg" : "succesfully added"
    }
    return jsonify(res)
app.run(host='localhost', port=port)

