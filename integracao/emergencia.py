import time
import Blockchain

def emergencia() -> None:
  bChain = Blockchain()
  while true:
    x , y , z = GerarPontos()
    tempo = time.now()
    preHash = bChain.lastNode().hash
    block = {
       'x': 'x',
       'y': 'y',
       'z': 'z',
       'time':tempo,
       'preHash': preHash,
       'hash': bChain.digest(tempo,preHash)
       ''
       }
    a, b = emergencia()
    if a:
      print("quer voltar manualmente?")
      opcao = input()
      if opcao:
        return
      else:
      voltarAutomatico(bChain)
      return
    else if b:
      voltarAutomatico(bChain)
      return
