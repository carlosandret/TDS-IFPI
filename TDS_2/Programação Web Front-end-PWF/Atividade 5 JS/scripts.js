function getById(id) {
  return document.getElementById(id);
}


function ocultar() {
    paragrafo = getById('paragrafo');
    paragrafo.style.visibility = 'hidden';
}

function mostrar() {
    paragrafo.style.visibility = 'visible';
}   