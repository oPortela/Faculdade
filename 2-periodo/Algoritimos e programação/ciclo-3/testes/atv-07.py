creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']

def names_vowels(x):
  return x[0].lower() in 'aeiou'

filtered_names = filter(names_vowels, creature_names)

print(list(filtered_names))


def filtrar_por_letra(nomes_estudantes):
    return nomes_estudantes[0].lower() in filtro

filtro = input('Digite a letra que deseja pesquisar: ')

nomes_filtrados = filter(filtrar_por_letra, nomes_estudantes)

print(f'Os nomes filtradoes que começam pela letra {filtro} são os {list(nomes_filtrados)}')