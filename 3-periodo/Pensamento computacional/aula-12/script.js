document.getElementById('imcForm').addEventListener('submit', function(event){
    event.preventDefault();

    var peso = parseFloat(document.getElementById('ipeso').value);
    var altura = parseFloat(document.getElementById('ialtura').value) / 100;

    var calcularImc = peso / (altura * altura);

    var mensagem = '';
    if (calcularImc < 18.5) {
        mensagem = 'Seu IMC é de ' + calcularImc.toFixed(2) + ', você possui um índice de Magreza alto.';
    }
    
    document.getElementById('resultado').innerText = mensagem;
});
