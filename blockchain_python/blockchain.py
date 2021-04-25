import hashlib
import time

class Blockchain:
    chain: list

    def __init__(self):

        with open("blockchain_data.csv", "w") as fp:
            fp.write("hash; preHash; time; locationX; locationY; locationZ;\n")
            actualTime = time.time()
            hashNode = hashlib.sha256()
            hashNode.update(f"{actualTime}init".encode())

            fp.write(f"{hashNode.hexdigest()};init;{time.ctime(actualTime)};init;init;init")

    # def save(self, tup):

    # def addNode(self, tup):
    
    # def lastNode(self):
    
Blockchain = Blockchain()
