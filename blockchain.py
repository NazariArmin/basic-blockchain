from time import time 
from .proof_of_work import *
class Blockvahin:
    def __init__(self):
        chain = []
        mempool = []
    
    def add_block(self, block):
        self.chain.append(block)
        return self.chain
    
    def get_block():
        block = {"index": len(self.chain),
                 "transaction": self.mempool,
                 "time": time(),
                 "bounce" : 0
                 "previouse_hash": hash(self.last_block)
                 }   
        return block
    @property
    def last_block(self):
        return self.chain[-1]