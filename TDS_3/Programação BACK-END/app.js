const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Olá Mundo!')
})

app.get('/carlos', (req, res) => {
  res.send('Olá Carlos!')
})

app.get('/home', (req, res) => {
  res.send('Minha página!')
})


app.listen(port, () => {
  console.log(`App de exemplo esta rodando no endereço http://localhost:${port}/`)
})