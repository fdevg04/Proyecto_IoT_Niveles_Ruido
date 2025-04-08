# Proyecto IoT: Niveles de Ruido en Provincias de Costa Rica

Este proyecto simula un sistema IoT para la monitorización de niveles de ruido en distintas provincias de Costa Rica. Incluye la simulación de niveles de ruido, la publicación de datos mediante MQTT, su procesamiento en la herramienta Node-RED, y la notificación de alertas mediante un bot de Telegram. Además, permite visualizar los datos en un dashboard interactivo.

---

## Requisitos Previos

Para ejecutar el programa de manera correcta, se deberán tener instalados los siguientes programas en la máquina respectiva:

1. **Python 3.x** y los módulos necesarios:
   - `paho-mqtt`
   - `matplotlib`

2. **Node.js** y **Node-RED**.
3. **Broker MQTT (Mosquitto)**.
4. **Cuenta de Telegram** y buscar el bot NoiseBot (`@noiseTEC_bot`) en la aplicación.

---

## Estructura del Proyecto

La carpeta principal contiene los siguientes archivos:

- `publicador_mqtt.py`: Código para simular y publicar niveles de ruido mediante MQTT.
- `simulacion_microfono.py`: Código que simula niveles de ruido en tiempo real.
- `bot_code.js`: Código JavaScript para procesar alertas en Node-RED y enviar mensajes con el bot de Telegram.
- `flujo_niveles_ruido_node.json`: Archivo JSON que contiene el flujo de Node-RED para importar.
- `links_node_red.txt`: Archivo con los enlaces del Node-RED y del dashboard.
- `package-lock.json`: Archivo de configuración de Node.js.
- `token_bot_API`: Archivo de texto con el token del bot de Telegram.

---

## Pasos para Ejecutar el Proyecto

### 1. Instalar y Configurar Mosquitto

1. **Descargar e instalar Mosquitto:**
   - En **Windows**:
     - Descargar el instalador desde [Eclipse Mosquitto](https://mosquitto.org/).
     - Durante la instalación, selecciona la opción de instalar el servicio.

2. **Iniciar el servicio Mosquitto:**
   - Ejecutar el siguiente comando en PowerShell:
     ```bash
     net start mosquitto
     ```
3. **Asegurarse de que Mosquitto esté corriendo en el puerto 1883 (por defecto).**

---

### 2. Configurar el Entorno de Python

1. Instalar **Python 3.x** en tu computadora.
2. Instalar los módulos requeridos ejecutando:
   ```bash
   pip install paho-mqtt matplotlib

---

### 3. Configurar y Ejecutar los Scripts de Python

1. **simulacion_microfono.py**:  
   Este script simula niveles de ruido y los muestra en una gráfica en tiempo real.  
   Para ejecutarlo, abrir la terminal y ejecutar el siguiente comando:
   ```bash
   python simulacion_microfono.py
2. **publicador_mqtt.py**:
    Publica datos de ruido (incluyendo provincias) en el tópico `ciudad/ruido`.
    Ejecutar el script:
    ```bash
    python publicador_mqtt.py

---

### 4. Configurar Node-RED

1. **Abrir una terminal y ejecutar**:
    ```bash
    node-red
2. **Importar el flujo**:
    - Abrir Node-RED en el navegador: http://localhost:1880.
    - Ir a Menú > Import > Archivo y selecciona el archivo `flujo_niveles_ruido_node.json`.
    - Verificar que el flujo se importe correctamente.
3. **Configurar la función del bot**:
    - Abrir el nodo function llamado `Noise`.
    - Copiar y pegar el contenido del archivo `bot_code.js` en la función.
4. **Ajustar el nodo HTTP request (en caso de ser necesario)**:
    - Configurar el token del bot en el nodo HTTP:
    ```bash
    https://api.telegram.org/bot<TU_TOKEN>/sendMessage
    ```
    **(Reemplazar <TU_TOKEN> con el token real).**
5. **Iniciar el flujo**:
    - Presionar el botón **"Deploy"** para activar el flujo.
    - Asegurarse de que Node-RED esté conectado al broker MQTT.

---

### 5. Configurar el Dashboard

1. Configurar el Dashboard
2. Asegurarse de que el gráfico (chart) esté correctamente configurado:
    - **Eje X:** Muestra el tiempo.
    - **Eje Y:** Niveles de ruido (30-120 dB).
3. Para acceder al dashboard, usa el enlace especificado en `links_node_red.txt`.

---

### 6. Uso del Bot de Telegram

1. Enviar un mensaje de inicio (`/start`) al bot para inicializar.
2. Se recibirán alertas de ruido cuando se detecten niveles superiores al umbral (100 dB).

---

### 7. Verificación del Funcionamiento

1. Abrir el script `publicador_mqtt.py` y verificar que los datos incluyan ubicaciones, además de los datos de ruido.
2. En Node-RED, verificar que las alertas se muestren en el chat del bot y que el gráfico del dashboard se actualice en tiempo real.