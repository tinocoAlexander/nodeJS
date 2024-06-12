const express = require ('express');
const app = express();

app.get('/', (req, res)=>{
    res.send("Hola mundo 2");
})

app.listen(5000, ()=>{
    console.log("Escuchando en el puerto 5000");
})