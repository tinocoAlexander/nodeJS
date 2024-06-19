const express = require ('express');
const mysql = require('mysql2')
const app = express();
const db = mysql.createPool({
    host:'localhost',
    user: 'tinoquito',
    password:'123',
    database:'controlescolar',
});

app.get('/', (req, res)=>{
    res.send("Hola mundo 2");
})
app.get('/profesores', (req, res)=>{
    const respuesta = {
        "id":5,
        "nombre": "dagoberto fiscal",
        "correo": "dago@gmail.com",
        "direccion": "5 de febrero 100",
        "telefono": "6181232323",
    }
    res.status(200).send(respuesta);
})

app.all('*', (req, res) =>{
    res.send("La ruta no existe")
})
app.listen(5000, ()=>{
    console.log("Escuchando en el puerto 5000");
})