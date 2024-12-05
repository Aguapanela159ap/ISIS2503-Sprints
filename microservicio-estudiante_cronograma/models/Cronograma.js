const mongoose = require('mongoose');

const CronogramaSchema = new mongoose.Schema({
    codigo: { type: String, required: true, unique: true },
    listaGrados: { type: [String], required: true }, // Ejemplo: ["Primero", "Segundo"]
    costo: { type: Number, required: true },
    fechaCausacion: { type: Date, required: true },
    tipoPago: { type: String, required: true } // Ejemplo: "Mensual" o "Anual"
});

module.exports = mongoose.model('Cronograma', CronogramaSchema);
