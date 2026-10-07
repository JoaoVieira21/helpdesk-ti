function carregarChamados() {
    fetch("/chamados")
        .then(resposta => resposta.json())
        .then(chamados => {

            const lista = document.getElementById("lista-chamados");

            lista.innerHTML = "";

            chamados.forEach(chamado => {

                const item = document.createElement("div");

                item.classList.add("chamado");

                item.innerHTML = `
                    <h3>${chamado.titulo}</h3>

                    <p>${chamado.descricao}</p>

                    <div class="informacoes">
                        <span class="prioridade">
                            Prioridade: ${chamado.prioridade}
                        </span>

                        <span class="status">
                            Status: ${chamado.status}
                        </span>
                    </div>
                `;

                lista.appendChild(item);
            });
        });
}


carregarChamados();

document.addEventListener("change", function(event) {

    if (event.target.classList.contains("alterar-status")) {

        const id = event.target.dataset.id;
        const novoStatus = event.target.value;

        fetch(`/chamados/${id}`, {
            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                status: novoStatus
            })
        })

        .then(resposta => resposta.json())

        .then(resultado => {
            alert(resultado.mensagem);
            carregarChamados();
        });
    }
});
document.getElementById("form-chamado").addEventListener("submit", function(event) {

    event.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const descricao = document.getElementById("descricao").value;
    const prioridade = document.getElementById("prioridade").value;

    fetch("/chamados", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            titulo: titulo,
            descricao: descricao,
            prioridade: prioridade
        })
    })

    .then(resposta => resposta.json())

    .then(resultado => {

        alert(resultado.mensagem);

        document.getElementById("form-chamado").reset();

        carregarChamados();
    });
});