function getById(id) {
    return document.getElementById(id);
}

let alterarFundo = getById('alterarFundo');

alterarFundo.addEventListener('click', () => {
    getById('caixaFundo').style.backgroundColor = 'green';
})

let fontFamilyOriginal;
let fontSizeOriginal;
let mudou = false;

let alterarFonte = getById('alterarFonte');
alterarFonte.addEventListener('click', () => {
    let texto = getById('texto');

    if (!mudou) {
        fontFamilyOriginal = texto.style.fontSize;
        fontSizeOriginal = texto.style.fontFamily;

        texto.style.fontSize = '40px';
        texto.style.fontFamily = 'Arial';

        mudou = true;

    } else {
        texto.style.fontSize = fontFamilyOriginal;
        texto.style.fontFamily = fontSizeOriginal;
        mudou = false;
    }
    
})