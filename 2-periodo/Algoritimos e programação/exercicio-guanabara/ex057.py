sexo = str(input('Informe o seu sexo [M/F]: ')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o seu sexo novamente [M/F]: ')).upper()
if sexo == 'M':
    sx = 'Masculino'
else: 
    sx = 'Feminino'
print(f'O seu sexo é: {sx}.')
