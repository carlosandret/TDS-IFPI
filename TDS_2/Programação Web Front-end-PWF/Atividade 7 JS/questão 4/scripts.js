function getByID(id) {
return document.getElementById(id);
}

let botaoConsultar = getByID('botaoConsultar');
botaoConsultar.addEventListener('click', consultarPreco);
async function consultarPreco() {
let moedaBase = getByID('moedaBase').value.toUpperCase(); // Moeda base (ex.: BTC)
let moedaConversao = getByID('moedaConversao').value.toUpperCase(); // Moeda de
conversão (ex.: USDT)
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
}
