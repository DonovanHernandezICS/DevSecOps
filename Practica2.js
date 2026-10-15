// Ejemplo de código inseguro en app.js
const usuario = req.query.username;
// Vulnerabilidad: Inyección de código mediante eval()
eval("console.log('Usuario conectado: ' + " + usuario + ");");
