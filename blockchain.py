from time import time 
from .proof_of_work import hash
class Blockchain:
    def __init__(self):
        chain = []
        mempool = []
        get_block(first_blcok=True)
    
    def add_block(self, block):
        self.chain.append(block)
        return self.chain

    def get_block(first_block=False):
        block = {
                    "index": len(self.chain),
                    "transaction": self.mempool,
                    "time": time(),
                    "bounce" : 0
                    "previouse_hash": not first_block or hash(self.last_block)
                }   
        return block
    
    def new_transaction(self, sender, receiver, amount):
        new_trx = {
            "sender" : sender, 
            "receiver" : receiver,
            "amount" : amount,
        }
        self.mempool.append(new_trx)


    @property
    def last_block(self):
        return self.chain[-1]