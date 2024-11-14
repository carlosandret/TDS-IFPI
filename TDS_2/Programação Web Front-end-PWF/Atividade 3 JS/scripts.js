function getById(id) {
    return document.getElementById(id);
}

// Questão 01

var botao01 = getById('botao01');
botao01.addEventListener('click', adicionaZero);
function adicionaZero() {
    var resultado01 = getById('resultado01');
    let numero1 = getById('numero1').value;
    numero1 = numero1.padStart(6,"0");
    resultado01.innerHTML = numero1;
}




