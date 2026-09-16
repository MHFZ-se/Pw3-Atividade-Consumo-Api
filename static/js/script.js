const lista = document.getElementById("carrosselLista");
const btnAnterior = document.getElementById("btnAnterior");
const btnProximo = document.getElementById("btnProximo");

const quantidadeObras = lista.children.length;

let posicao = 0;
let intervalo;
let timeoutRetorno;

function atualizarCarrossel() {
    lista.style.transform = `translateX(-${posicao * 20}%)`;
}

function proximo() {
    if (posicao < quantidadeObras - 5) {
        posicao++;
    } else {
        posicao = 0;
    }

    atualizarCarrossel();
}

function anterior() {
    if (posicao > 0) {
        posicao--;
    } else {
        posicao = quantidadeObras - 5;
    }

    atualizarCarrossel();
}

function iniciarCarrossel() {
    clearInterval(intervalo);

    intervalo = setInterval(() => {
        proximo();
    }, 5000);
}

function pausarCarrossel() {
    clearInterval(intervalo);
    clearTimeout(timeoutRetorno);

    timeoutRetorno = setTimeout(() => {
        iniciarCarrossel();
    }, 15000);
}

btnProximo.addEventListener("click", () => {
    proximo();
    pausarCarrossel();
});

btnAnterior.addEventListener("click", () => {
    anterior();
    pausarCarrossel();
});

iniciarCarrossel();