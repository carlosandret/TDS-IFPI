// Todas as rotas devem ser definidas neste arquivo.
const express = require('express')
// Importa a mini aplicação de roteamento do express.
const router = express.Router()

router.get('/', (req, res) => {
    res.render('home')
})

router.get('/livro_form', (req, res) => {
    res.render('livro_form')
})

router.post('/livro', (req, res) => {
    titulo = req.body.titulo
    autor = req.body.autor
    ano = Number(req.body.ano)
    genero = req.body.genero

    livro = {
        titulo: titulo,
        autor: autor,
        ano: ano,
        genero: genero 
    }
    livros = []
    livros.push(livro)
    res.render('livro_resposta', {livros: livros})
})

router.get('/livro_resposta', (req, res) => {
    res.render('livro_resposta')
})

// Exporta o roteador para ser utilizado em outros arquivos.
module.exports = router
