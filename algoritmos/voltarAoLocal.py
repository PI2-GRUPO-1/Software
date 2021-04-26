import Blockchain

def retornoAoLocal() -> None:
  bChain = Blockchain()

  if ocorreuEmergencia(bChain):
    print('quer voltar ao local onde ocorreu a emergencia?')
    opcao = input()
    if opcao:
      irAutomatico(bChain)

