const express = require('express');
const mysql = require('mysql2');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');

app.use(bodyParser.json());
app.use(cors());

const db = mysql.createConnection({
    host: '189.197.187.187',
    user: 'alumnos',
    password: 'Alumnos1010$',
    database: 'controlescolar',
});

app.get('/', (req, res) => {
    res.send("Hola mundo 2");
});

app.get('/profesores', (req, res) => {
    const sql = 'SELECT * FROM profesores';
    db.query(sql, (err, result) => {
        if (!err) {
            res.status(200).send(result);
        } else {
            res.status(500).send(err);
        }
    });
});

app.get('/profesor/:id', (req, res) => {
    const identificador = req.params.id;
    const sql = 'SELECT * FROM profesores WHERE id = ?';
    db.query(sql, [identificador], (err, result) => {
        if (!err) {
            res.status(200).send(result);
        } else {
            res.status(500).send(err);
        }
    });
});

app.post('/profesor/registrar', (req, res) => {
    const { id, nombre, correo, direccion } = req.body;
    const sql = 'INSERT INTO profesores (id, nombre, correo, direccion) VALUES (?, ?, ?, ?)';
    db.query(sql, [id, nombre, correo, direccion], (err, result) => {
        if (!err) {
            res.status(200).send({
                result,
                mensaje: 'Profesor registrado',
            });
        } else {
            res.status(500).send({
                err,
                mensaje: 'No se registró el profesor',
            });
        }
    });
});

app.delete('/profesor/eliminar/:id', (req, res) => {
    const identificador = req.params.id;
    const sql = 'DELETE FROM profesores WHERE id = ?';
    db.query(sql, [identificador], (err, result) => {
        if (!err) {
            res.status(200).send(result);
        } else {
            res.status(500).send(err);
        }
    });
});

app.put('/profesor/modificar', (req, res) => {
    const { id, nombre, correo, direccion } = req.body;
    const sql = 'INSERT INTO profesores (id, nombre, correo, direccion) VALUES (?, ?, ?, ?)';
    db.query(sql, [id, nombre, correo, direccion], (err, result) => {
        if (!err) {
            res.status(200).send({
                result,
                mensaje: 'Profesor registrado',
            });
        } else {
            res.status(500).send({
                err,
                mensaje: 'No se registró el profesor',
            });
        }
    });
});

app.all('*', (req, res) => {
    res.send("La ruta no existe");
});

app.listen(5000, () => {
    console.log("Escuchando en el puerto 5000");
});
