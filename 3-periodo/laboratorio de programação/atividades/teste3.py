class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Função para fazer o animal fazer som
def fazer_som_do_animal(animal):
    print(animal.fazer_som())

# Instanciando objetos
cachorro = Cachorro()
gato = Gato()

# Chamando a função com diferentes tipos de objetos
fazer_som_do_animal(cachorro)  # Saída: "Au au!"
fazer_som_do_animal(gato)      # Saída: "Miau!"
