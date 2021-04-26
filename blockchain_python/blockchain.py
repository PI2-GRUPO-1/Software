#!/usr/bin/env python3
import hashlib
import time
import csv
import datetime as dt
import asyncio
import os

class Blockchain():
    chain: list
    emergency : bool
    pathFile : str

    def __init__(self, emergency = False, pathFile = 'blockchain_data.csv'):
        self.emergency = emergency
        self.pathFile = pathFile
        try: 
            self.chain = []

            with open(self.pathFile, "r") as fp:
                reader = csv.DictReader(fp, delimiter=';')
                self.chain = list(reader)
                for x in self.chain:
                    t = dt.datetime.strptime(x['time'], "%a %b %d %H:%M:%S %Y")              
                    x['time'] = t.timestamp()


        except OSError:
            with open(self.pathFile, "w") as fp:
                fp.write("hash;preHash;time;locationX;locationY;locationZ;\n")
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
        with open(self.pathFile, "a") as fp:
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

    def deleteFile(self):
        os. remove(self.pathFile) 
    
    async def send(self, node):
        print(node)

    async def backTrack(self):
        if self.emergency:
            for x in reversed(self.chain):
                await self.send(x)
            

if __name__ == "__main__":
    Blockchain = Blockchain(True, 'blockchain_data.csv')
    Blockchain.emergency = True
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
    
    asyncio.run(Blockchain.backTrack())
    # Blockchain.deleteFile()
