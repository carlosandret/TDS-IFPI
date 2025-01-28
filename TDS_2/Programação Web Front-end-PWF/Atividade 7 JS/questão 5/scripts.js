function getByID(id) {
    return document.getElementById(id);
}

let botaoProcurar = getByID('botaoProcurar');
botaoProcurar.addEventListener('click', procurarPais);

async function procurarPais() {
    let nomePais = getByID('nomePais').value.toLowerCase(); // Nome do país digitado
    let resultado = getByID('resultado');
    let url = `https://restcountries.com/v3.1/name/${nomePais}`;

    let response = await fetch(url); // Faz a requisição à API
    if (!response.ok) {
        throw new Error(`Erro HTTP: ${response.status} - ${response.statusText}`);
    }
    let json = await response.json();

    // Verifica se retornou dados e exibe informações relevantes
    let pais = json[0]; // O primeiro país na resposta
    resultado.innerHTML = `
        <p><strong>Nome do país:</strong> ${pais.name.common}</p>
        <p><strong>Capital:</strong> ${pais.capital ? pais.capital[0] : 'Não disponível'}</p>
        <p><strong>Região:</strong> ${pais.region}</p>
        <p><strong>População:</strong> ${pais.population}</p>
        <p><strong>Bandeira:</strong> <img src="${pais.flags.svg}" alt="Bandeira de ${pais.name.common}" width="100"></p>
`;
}

let botaoEmoji = document.getElementById('botaoEmoji');
botaoEmoji.addEventListener('click', async () => {
    let url = 'https://emojihub.yurace.pro/api/random'; 
    let resultado1 = document.getElementById('resultado1'); 
    try {
        let response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Erro ao buscar o emoji: ${response.status}`);
        }
        let data = await response.json();
        resultado1.innerHTML = `Emoji: ${data.htmlCode.join('')} - Nome: ${data.name}`;
    } catch (error) {
        resultado1.innerHTML = `Erro: ${error.message}`;
    }
});
