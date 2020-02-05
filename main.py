from flask import Flask, jsonify, request
from blockchain import Blockchain
from sys import argv
from proof_of_work import proof_of_work

my_block_chain = Blockchain()
app = Flask(__name__)
port = int(argv[1])

@app.route('/mine')
def mine():
    my_block_chain.new_transaction(
        sender='base',
        receiver='armin',
        amount=25,
    )
    new_block = my_block_chain.get_block()
    new_block = proof_of_work(new_block)
    my_block_chain.add_block(new_block)
    return get_chain()

@app.route('/chain')
def get_chain():
    res = {
        "chain":my_block_chain.get_chain
    }
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

