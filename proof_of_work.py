from hashlib import sha256
from time import time 
import json 


def hash(block):
    json_block = json.dumps(block, sort_keys=True).encode()
    return sha256(json_block).hexdigest()

def proof_of_work(block):
    block['bounce'] = 0
    while not check_proof(block):
        block['bounce'] += 1
    return block    
def check_proof(block):
    this_proof = hash(block)
    return this_proof[-5:] == '00000'


transaction = {"sender": "armin",
               "receiver": "amin",
               "amount": 12}
my_block = {"index": 0,
            "timestamp": time(),
            "transaction": transaction}

accepted_block = proof_of_work(my_block)
print(accepted_block)
print(hash(accepted_block))