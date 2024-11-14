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

// Questão 02
var botao02 = getById('botao02');
botao02.addEventListener('click', CliqueBotao02);
function CliqueBotao02() {
    let resultado02 = getById('resultado02');
    let n1 = parseInt(getById('numero2').value);
    let n2 = parseInt(getById('numero3').value);
    let soma = n1 + n2;
    let subtracao = n1-n2;
    let multiplicacao = n1*n2;
    let divisao = n2 !== 0 ? (n1 / n2).toFixed(2) : "Divisão por zero indefinida";
    resultado02.innerHTML = 
        `<br>Resultados: <br>
        ${n1} + ${n2} = ${soma}<br>
        ${n1} - ${n2} = ${subtracao}<br>
        ${n1} x ${n2} = ${multiplicacao}<br>
        ${n1} / ${n2} = ${divisao}<br>
        `
}

// Questão 03
var botao03 = getById('botao03');
botao03.addEventListener('click', cliqueBotao03);
function cliqueBotao03() {
    var resultado03 = getById('resultado03');
    var temp_c = parseInt(getById('temperaturaCelsius').value);
    var temp_f = (temp_c * 1.8) + 32
    resultado03.innerHTML = 
    `<br>${temp_c}°C corresponde a ${temp_f}°F<br>`
}

// Questão 04
var botao04 = getById('botao04');
botao04.addEventListener('click', CliqueBotao04);
function CliqueBotao04() {
    resultado04 = getById('resultado04');
    const data = new Date();
    let dia = data.getDate();
    let mes = data.getMonth() + 1;
    let ano = data.getFullYear();

    resultado04.innerHTML = `${dia}/${mes}/${ano}`;
}

// Questao 05
var caixaTexto1 = getById('caixaTexto1');
caixaTexto1.addEventListener('keyup', funcao);
function funcao (){
    let caixaTexto2 = getById('caixaTexto2');
    caixaTexto2.value = caixaTexto1.value;
}
