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


function carregarChamados() {

    fetch("/chamados")

        .then(resposta => resposta.json())

        .then(chamados => {

            const lista = document.getElementById("lista-chamados");

            lista.innerHTML = "";


            // DASHBOARD

            document.getElementById("total-chamados").textContent =
                chamados.length;

            document.getElementById("chamados-abertos").textContent =
                chamados.filter(chamado => chamado.status === "Aberto").length;

            document.getElementById("chamados-atendimento").textContent =
                chamados.filter(chamado => chamado.status === "Em atendimento").length;

            document.getElementById("chamados-resolvidos").textContent =
                chamados.filter(chamado => chamado.status === "Resolvido").length;


            // LISTA DE CHAMADOS

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

                    <select class="alterar-status" data-id="${chamado.id}">

                        <option value="Aberto"
                            ${chamado.status === "Aberto" ? "selected" : ""}>
                            Aberto
                        </option>

                        <option value="Em atendimento"
                            ${chamado.status === "Em atendimento" ? "selected" : ""}>
                            Em atendimento
                        </option>

                        <option value="Resolvido"
                            ${chamado.status === "Resolvido" ? "selected" : ""}>
                            Resolvido
                        </option>

                    </select>
                `;

                lista.appendChild(item);

            });

        });
}


// CARREGAR CHAMADOS AO ABRIR A PÁGINA

carregarChamados();


// ALTERAR STATUS

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


// ABRIR NOVO CHAMADO

document.getElementById("form-chamado").addEventListener(
    "submit",
    function(event) {

        event.preventDefault();


        const titulo =
            document.getElementById("titulo").value;

        const descricao =
            document.getElementById("descricao").value;

        const prioridade =
            document.getElementById("prioridade").value;


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

            document
                .getElementById("form-chamado")
                .reset();

            carregarChamados();

        });

    }
);
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