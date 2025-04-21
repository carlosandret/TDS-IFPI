// Todas as rotas devem ser definidas neste arquivo.
const express = require('express');
// Importa a mini aplicação de roteamento do express.
const router = express.Router();

router.use(express.urlencoded({ extended: false }));

router.get('/', (req, res) => {
    res.render('home')
})

router.get('/registro', (req, res) => {
    res.render('registro')
})

router.post('/registro', (req, res) => {
    res.render('registro')
})

router.get('/resposta_registro', (req, res) => {
    res.render('resposta_registro')
})



module.exports = router;