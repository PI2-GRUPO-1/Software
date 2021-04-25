#!/usr/bin/env python3
import hashlib
import time

class Blockchain:
    chain: list

    def __init__(self):
        with open("blockchain_data.csv", "w") as fp:
            fp.write("hash; preHash; time; locationX; locationY; locationZ;\n")
            actualTime = time.time()
            hashDigest = self.digest(actualTime, 'init')
            fp.write(f"{hashDigest};init;{time.ctime(actualTime)};init;init;init;\n")
            self.chain = [{
                'hash': hashDigest,
                'preHash': 'init',
                'time': actualTime,
                'locationX': 'init',
                'locationY': 'init',
                'locationZ': 'init'
            }]

    def save(self, dicto:dict):
        with open("blockchain_data.csv", "a") as fp:
            fp.write(f"{dicto['hash']};{dicto['preHash']};{dicto['time']};{dicto['locationX']};{dicto['locationY']};{dicto['locationZ']};\n")
    def addNode(self, dicto:dict):
        self.save(dicto)
        self.chain.append(dicto)
    def lastNode(self):
        return self.chain[-1]
    def digest(self,MyTime, preHash):
        hashNode = hashlib.sha256()
        hashNode.update(f"{MyTime}{preHash}".encode())
        return hashNode.hexdigest()
if __name__ == "__main__":
    Blockchain = Blockchain()
    for i in range(10):
        MyTime = time.time()
        preHash = Blockchain.lastNode()['hash']
        node = {'hash': Blockchain.digest(MyTime, preHash),
                'preHash': preHash,
                'time': time.ctime(MyTime),
                'locationX': i,
                'locationY': i,
                'locationZ': i}
        
        Blockchain.addNode(node)
