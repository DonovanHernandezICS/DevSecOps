
const express = require('express');
const app = express();

app.get('/usuario', (req, res) => {
    // Fuente de datos no confiables: parámetro HTTP
    const username = req.query.username;

    // Vulnerabilidad: ejecución de código mediante eval()
    eval("console.log('Usuario conectado: ' + '" + username + "')");

    res.send('Usuario procesado');
});

app.listen(3000, () => {
    console.log('Servidor iniciado en el puerto 3000');
});
