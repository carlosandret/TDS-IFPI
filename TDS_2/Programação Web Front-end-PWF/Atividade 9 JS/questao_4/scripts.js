function getByID(id) {
return document.getElementById(id);
}

let botaoConsultar = getByID('botaoConsultar');
botaoConsultar.addEventListener('click', consultarPreco);
async function consultarPreco() {
    let moedaBase = getByID('moedaBase').value.toUpperCase(); // Moeda base (ex.: BTC)
    let moedaConversao = getByID('moedaConversao').value.toUpperCase(); // Moeda de conversão (ex.: USDT)
    let resultado = getByID('resultado');
    let url =
    `https://api.binance.com/api/v3/ticker/price?symbol=${moedaBase}${moedaConversao}`;
try {
let response = await fetch(url); // Faz a requisição à API Binance
if (!response.ok) {
throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
}
let json = await response.json();

resultado.innerHTML = `
<p><strong>Par de Moedas:</strong> ${json.symbol}</p>
<p><strong>Preço:</strong> ${parseFloat(json.price).toFixed(2)}
${moedaConversao}</p>`;
} catch (error) {
resultado.innerHTML = 'Erro: ' + error.message;
}
};

// a) Botão para limpar os campos
let botaoLimparCampos = getByID('botaoLimparCampos');
botaoLimparCampos.addEventListener('click', ()=> {
    moedaBase.value = '';
    moedaConversao.value = '';
    resultado.innerHTML = '';
});

// b) Botão de inverter moedas: Um botão que troca os valores das moedas base e de conversão;
let boataoInverterValor = getByID('botaoInverteValor');
boataoInverterValor.addEventListener('click', ()=> {
    let moedaBase = getByID('moedaBase');
    let moedaConversao = getByID('moedaConversao');

    let moedaTemp = moedaBase.value;
    moedaBase.value = moedaConversao.value;
    moedaConversao.value = moedaTemp;   
});




