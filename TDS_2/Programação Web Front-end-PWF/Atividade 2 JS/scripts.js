var botao1 = document.getElementById('botao1');
botao1.addEventListener('click', CliqueDoBotao1);

function CliqueDoBotao1() {
    var resultado1 = document.getElementById('resultado1');
    resultado1.innerHTML = 'Olá, Boa tarde!!';
}

var botao2 = document.getElementById('botao2');
botao2.addEventListener('click', CliqueDoBotao2);

function CliqueDoBotao2() {
    var resultado2 = document.getElementById('resultado2');
    resultado2.innerHTML = 'Olá, Boa noite!!';
}

var botao3 = document.getElementById('botao3');
botao3.addEventListener('click', CliqueDoBotao3);

function CliqueDoBotao3() {
    var resultado3 = document.getElementById('resultado3');
    var caixaTextoNome = document.getElementById('caixaTextoNome');
    var texto = caixaTextoNome.value;
    resultado3.innerHTML = 'É um prazer  conhecê lo, ' + texto +'!';

}

var botao4 = document.getElementById('botao4');
botao4.addEventListener('click', CliqueDoBotao4);
function CliqueDoBotao4(){
    var resultado4 = document.getElementById('resultado4');
    var num = resultado4.value
    resultado4.innerHTML = Math.round((Math.random() * 10)+ 1);
}

var botao5 = document.getElementById('botao5');
botao5.addEventListener('click', CliqueDoBotao5);
function CliqueDoBotao5() {
    var resultado5 = document.getElementById('resultado5');
    var caixatexto1 = document.getElementById('caixatexto1');
    var num = caixatexto1.value;
    resultado5.innerHTML = Math.abs(num);
}

var botao6 = document.getElementById('botao6');
botao6.addEventListener('click', CliqueDoBotao6);
function CliqueDoBotao6() {
    var resultado6 = document.getElementById('resultado6');
    var numero1 = document.getElementById('caixatexto2').value;
    var numero2 = document.getElementById('caixadetexto3').value;
    resultado6.innerHTML = Math.max(numero1, numero2);
} 

var botao7 = document.getElementById('botao7');
botao7.addEventListener('click', CliqueDoBotao7);
function CliqueDoBotao7() {
    var resultado7 = document.getElementById('resultado7');
    var numero1 = document.getElementById('caixatexto4').value;
    resultado7.innerHTML = 'O valor arredondado é ' +Math.round(numero1);
} 

var botao8 = document.getElementById('botao8');
botao8.addEventListener('click', CliqueDoBotao8);
function CliqueDoBotao8() {
    var resultado8 = document.getElementById('resultado8');
    var numero1 = document.getElementById('caixatexto5').value;
    var numero2 = document.getElementById('caixatexto6').value;
    resultado8.innerHTML = numero1 + ' elevado a ' + numero2 + ' é  igual a ' + Math.pow(numero1, numero2);
} 

var botao9 = document.getElementById('botao9');
botao9.addEventListener('click', CliqueDoBotao9);
function CliqueDoBotao9() {
    var palavra = document.getElementById('caixatexto7');
    document.getElementById('resultado9').innerHTML = palavra.length;
    // resultado9.innerHTML = 
} 