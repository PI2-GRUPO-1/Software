import time
import Blockchain
from typing import Optional

def mapping(bchain: Optional [BlockChain]) -> Blockchain:
  if !bchain:
    bChain = Blockchain()

  while true:
    x , y , z = GerarPontos()
    tempo = time.time()
    preHash = bChain.lastNode().hash
    block = {
       'x': 'x',
       'y': 'y',
       'z': 'z',
       'time':tempo,
       'preHash': preHash,
       'hash': bChain.digest(tempo,preHash)
       }
    if isNotPressed():
      return bChain
      
