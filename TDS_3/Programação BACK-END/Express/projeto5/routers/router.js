const express = require('express')
const router = express.Router()

router.get('/', (req, res) => {
    res.render('home')
})

router.get('/nova_operacao', (req, res) => {
    res.render('nova_operacao')
})

router.post('/nova_operacao', (req, res) => {
    data = req.body.data;
    codigo = req.body.codigo;
    tipo = req.body.tipo;
    quantidade = Number(req.body.quantidade);
    preco = Number(req.body.preco);
    valorBruto = quantidade * preco;
    valorLiquido = 0;
    console.log(quantidade)
    if (tipo == 'compra') {
        valorLiquido = valorBruto + ((valorBruto * 0.05) /100) 
    } else {
        valorLiquido = valorBruto - ((valorBruto * 0.05) /100) 
    }
    
    res.render('resposta_operacao', {
        data: data,
        codigo: codigo,
        tipo : tipo,
        quantidade : quantidade,
        preco : preco,
        valorBruto : valorBruto,
        valorLiquido : valorLiquido
    })
    
})

module.exports = router