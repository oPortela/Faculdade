arquivo = open('pessoas.txt','r')

for linha in arquivo:
	itens=linha.split()
	print("\n") 
	print("Nome:                    ", itens[0], itens[1])
	print("Endereço:                ", itens[2], itens[3], itens[4]) 
	print("Documento de Identidade: ", itens[5]) 
	print("Data de Nascimento:      ", itens[6]) 
	print("\n") 

arquivo.close()