const express = require('express');
const Cronograma = require('../models/Cronograma');
const router = express.Router();

// Crear un cronograma
router.post('/', async (req, res) => {
    try {
        const nuevoCronograma = new Cronograma(req.body);
        const cronogramaGuardado = await nuevoCronograma.save();
        res.status(201).json(cronogramaGuardado);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Obtener todos los cronogramas
router.get('/', async (req, res) => {
    try {
        const cronogramas = await Cronograma.find();
        res.status(200).json(cronogramas);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Editar un cronograma por ID
router.put('/:id', async (req, res) => {
    try {
        const cronogramaActualizado = await Cronograma.findByIdAndUpdate(
            req.params.id,
            req.body,
            { new: true }
        );
        res.status(200).json(cronogramaActualizado);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Eliminar un cronograma por ID
router.delete('/:id', async (req, res) => {
    try {
        await Cronograma.findByIdAndDelete(req.params.id);
        res.status(200).json({ message: 'Cronograma eliminado' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

module.exports = router;
