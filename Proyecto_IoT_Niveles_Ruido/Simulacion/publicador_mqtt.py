import random
import time
import paho.mqtt.client as mqtt
import json

# Configuración MQTT
BROKER = "localhost"  # Dirección del broker, "localhost" si estás en la misma máquina
TOPIC = "ciudad/ruido"  # Tema en el que publicaremos los datos
INTERVALO = 1  # Intervalo de tiempo entre publicaciones (en segundos)
PROVINCIAS = ["San Jose", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limon"]

# Función para generar niveles de ruido simulados y ubicación
def generar_dato():
    """Genera un nivel de ruido y una ubicación aleatoria."""
    nivel_ruido = random.uniform(30, 120)
    provincia = random.choice(PROVINCIAS)
    return {"ruido": nivel_ruido, "provincia": provincia}

# Conexión con el broker MQTT
cliente = mqtt.Client()
cliente.connect(BROKER, 1883, 60)

try:
    while True:
        dato = generar_dato()
        mensaje_json = json.dumps(dato)  # Convertir el diccionario a formato JSON
        print(f"Datos enviados: {mensaje_json}")
        
        # Publicar los datos en formato JSON en el topic
        cliente.publish(TOPIC, mensaje_json)
        
        # Espera antes de enviar el siguiente valor
        time.sleep(INTERVALO)

except KeyboardInterrupt:
    print("Publicación detenida.")
    cliente.disconnect()
