from time import time 
from proof_of_work import hash
class Blockchain:

    def __init__(self):
        self.chain = []
        self.mempool = []
        first_block = self.get_block(first_block=True)
        self.add_block(first_block)

    def add_block(self, block):
        self.chain.append(block)
        return self.chain

    def get_block(self, first_block=False):
        block = {
                    "index": len(self.chain),
                    "transaction": self.mempool,
                    "time": time(),
                    "bounce" : 0,
                    "previouse_hash": first_block or hash(self.last_block),
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
    def get_chain(self):
        print(self.chain)
        return self.chain
    @property
    def last_block(self):
        return self.chain[-1]