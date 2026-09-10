import threading
import time
import random

# ==========================================
# CONFIGURACIÓN DEL BÚFER
# ==========================================

TAMANO_BUFFER = 5

buffer = []

# Semáforos
espacios_disponibles = threading.Semaphore(TAMANO_BUFFER)
datos_disponibles = threading.Semaphore(0)



# Exclusión mutua
mutex = threading.Lock()


# ==========================================
# PRODUCTOR
# ==========================================

def productor(nombre_sensor):
    for i in range(5):

        dato = {
            "sensor": nombre_sensor,
            "vehiculos": random.randint(10, 100)
        }

        # Esperar un espacio disponible
        espacios_disponibles.acquire()

        # Acceso exclusivo al búfer
        with mutex:
            buffer.append(dato)

            print(
                f"{nombre_sensor} -> "
                f"Produciendo: {dato['vehiculos']} vehículos"
            )

            print(
                f"Búfer -> "
                f"{[d['vehiculos'] for d in buffer]}"
            )

        # Avisar que hay un dato disponible
        datos_disponibles.release()

        time.sleep(random.uniform(0.5, 1.5))


# ==========================================
# CONSUMIDOR
# ==========================================

def consumidor():
    for i in range(10):

        # Esperar hasta que exista un dato
        datos_disponibles.acquire()

        # Acceso exclusivo al búfer
        with mutex:
            dato = buffer.pop(0)

            print(
                f"Analizador -> "
                f"Consumiendo dato de {dato['sensor']}: "
                f"{dato['vehiculos']} vehículos"
            )

            print(
                f"Búfer -> "
                f"{[d['vehiculos'] for d in buffer]}"
            )

        # Liberar espacio del búfer
        espacios_disponibles.release()

        time.sleep(random.uniform(0.5, 1.5))
# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

print("\n==============================================")
print("     PRODUCTOR - CONSUMIDOR SIGET")
print("==============================================\n")

# Crear hilos productores
sensor1 = threading.Thread(
    target=productor,
    args=("Sensor 1",)
)

sensor2 = threading.Thread(
    target=productor,
    args=("Sensor 2",)
)

# Crear hilo consumidor
analizador = threading.Thread(
    target=consumidor
)

# Iniciar hilos
sensor1.start()
sensor2.start()
analizador.start()

# Esperar a que terminen
sensor1.join()
sensor2.join()
analizador.join()

print("\n==============================================")
print("       SIMULACIÓN FINALIZADA")
print("==============================================")