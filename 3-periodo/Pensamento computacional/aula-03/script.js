/*var teste = 'Olá mundo'

window.alert(teste)
window.confirm('Minha segunda mensagem!')
window.prompt('Qual o seu nome? ')
console.log('Teste teste')*/

var nome = prompt('Qual o seu nome: ')

var nota1 = Number.parseInt(prompt('Digite a primeira nota: '))
var nota2 = Number.parseInt(prompt('Digite a segunda nota: '))
var nota3 = Number.parseInt(prompt('Digite a terceira nota: '))

var media = (nota1 + nota2 + nota3) / 3


alert('Olá '+ nome + ' , é um prazer te conhecer!')
alert('Sua média foi de: ' + media)

if (media > 60) {
    alert('Você está aprovado!')
} else {
    alert('Você está reprovado!')
}

console.log(nome, media)