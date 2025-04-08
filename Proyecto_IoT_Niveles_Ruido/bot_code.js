const umbral = 100; // Define el umbral en decibelios

// Asignar una ubicación aleatoria (provincias de Costa Rica)
const provincias = ["San Jose", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limon"];
const provincia = provincias[Math.floor(Math.random() * provincias.length)]; // Selección aleatoria

// Evaluar si el nivel de ruido excede el umbral
if (msg.payload.ruido > umbral) {
    msg.payload = {
        chat_id: "1589031873", // tu chat ID
        text: "¡Alerta! Nivel de ruido alto detectado: " + msg.payload.ruido.toFixed(2) + " dB en " + provincia
    };
    return msg;
} else {
    return null;
}
