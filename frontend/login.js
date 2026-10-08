document.getElementById("form-login").addEventListener("submit", function(event) {

    event.preventDefault();

    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;

    const mensagem = document.getElementById("mensagem-login");

    mensagem.textContent = "Verificando login...";
    mensagem.style.color = "#6b7280";

    fetch("/login", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            email: email,
            senha: senha
        })
    })

    .then(resposta => resposta.json())

    .then(resultado => {

        mensagem.textContent = resultado.mensagem;

        if (resultado.sucesso) {

            mensagem.style.color = "#16a34a";

            setTimeout(() => {
                window.location.href = "/";
            }, 1000);

        } else {

            mensagem.style.color = "#dc2626";

        }

    })

    .catch(erro => {

        console.error(erro);

        mensagem.textContent = "Erro ao conectar com o servidor.";
        mensagem.style.color = "#dc2626";

    });

});