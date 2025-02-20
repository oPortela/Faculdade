document.getElementById('login-form').addEventListener('submit', function(event){
    event.preventDefault()

    var username = document.getElementById('username').value 
    var password = document.getElementById('password').value 

    if (username === 'matheus' && password === '123') {
        document.getElementById('mensagem').innerText = 'Login bem sucedido.';
        alert('Sucesso!')
        //location.href = 'home.html'
    } else {
        document.getElementById('mensagem').innerText = 'E-mail ou senha incorretos'
        alert('Erro')
    }
})