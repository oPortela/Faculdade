#Matheus Marques Portela - 2310823
#Marcos Paulo Moreira Damasceno - 2310004

capacidade_ram = 1000
blocos_livres = [(0, capacidade_ram)]
processos_alocados = []

def alocar_memoria(processo):
  global blocos_livres, processos_alocados

  for indice, bloco in enumerate(blocos_livres):
    if bloco[1] >= processo:
      endereco_memoria = bloco[0]
      tamanho_bloco = bloco[1]
      
      if tamanho_bloco > processo:
        blocos_livres.insert(indice + 1, (endereco_memoria + processo, tamanho_bloco - processo))
      blocos_livres.remove(bloco)

      processos_alocados.append((processo, endereco_memoria))

      return endereco_memoria

  return -1

def desaloca_memoria(processo):
  global blocos_livres, processos_alocados

  for processo_alocado in processos_alocados:
    if processo_alocado[0] == processo:
      endereco_memoria = processo_alocado[1]

      blocos_livres.append((endereco_memoria, processo))
      processos_alocados.remove(processo_alocado)
      
      combinar_blocos_livres()

      return True
  return False

def combinar_blocos_livres():
  global blocos_livres

  for indice in range(len(blocos_livres) - 1):
    bloco_atual = blocos_livres[indice]
    proximo_bloco = blocos_livres[indice + 1]

    if bloco_atual[1] + proximo_bloco[0] == proximo_bloco[1]:
      blocos_livres[indice] = (bloco_atual[0], bloco_atual[1] + proximo_bloco[1])
      del blocos_livres[indice + 1]

processos = [200, 400, 150, 300, 50, 25, 95, 49]
for processo in processos:
  endereco_memoria = alocar_memoria(processo)
  if endereco_memoria != -1:
    print(f"Processo {processo} alocado na memória: {endereco_memoria}")
  else:
    print(f"Processo {processo} não pôde ser alocado!")

print("\nEstado final da RAM:")
for bloco in blocos_livres:
  print(f"Bloco livre: {bloco}")
for processo_alocado in processos_alocados:
  print(f"Processo {processo_alocado[0]} alocado em: {processo_alocado[1]}")

fragmentacao_interna = 0
for bloco_livre in blocos_livres:
  fragmentacao_interna += bloco_livre[1]
fragmentacao_interna_porcentagem = (fragmentacao_interna / capacidade_ram) * 100
print(f"\nÍndice de fragmentação interna: {fragmentacao_interna_porcentagem:.2f}%")