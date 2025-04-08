import random
import time
import matplotlib.pyplot as plt

# Configuración de la simulación
MIN_RUIDO = 30  # Nivel mínimo de ruido (ejemplo: 30 dB)
MAX_RUIDO = 120  # Nivel máximo de ruido (ejemplo: 120 dB)
INTERVALO = 0.5  # Intervalo entre lecturas (en segundos)
PROVINCIAS = ["San Jose", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limon"]

def generar_dato():
    """Simula un nivel de ruido y una ubicación aleatoria."""
    nivel_ruido = random.uniform(MIN_RUIDO, MAX_RUIDO)
    provincia = random.choice(PROVINCIAS)
    return {"ruido": nivel_ruido, "provincia": provincia}

# Visualización en tiempo real
niveles_ruido = []
plt.ion()  # Activar modo interactivo
fig, ax = plt.subplots()
linea, = ax.plot(niveles_ruido, label="Nivel de ruido")
ax.set_ylim(MIN_RUIDO, MAX_RUIDO)
ax.set_title("Simulación de Nivel de Ruido")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Nivel de Ruido (dB)")
ax.legend()

try:
    while True:
        dato_actual = generar_dato()
        nivel_actual = dato_actual["ruido"]
        provincia_actual = dato_actual["provincia"]
        
        niveles_ruido.append(nivel_actual)
        print(f"Nivel de ruido simulado: {nivel_actual:.2f} dB en {provincia_actual}")
        
        # Actualizar gráfica
        if len(niveles_ruido) > 50:  # Mantener tamaño de la gráfica
            niveles_ruido.pop(0)
        linea.set_ydata(niveles_ruido)
        linea.set_xdata(range(len(niveles_ruido)))
        ax.relim()
        ax.autoscale_view()
        plt.pause(INTERVALO)

except KeyboardInterrupt:
    print("Simulación detenida.")
    plt.close()
