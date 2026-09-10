# productor_consumidor_siget
Tarea. Implementación de concurrencia en módulos

## Descripción

Este proyecto implementa una simulación del problema clásico de **Productor-Consumidor**, adaptado al contexto del **Sistema Inteligente de Gestión de Tráfico (SIGET)**.

La simulación representa sensores de tráfico que generan información y un módulo de análisis que consume y procesa esos datos mediante un búfer compartido.

El objetivo es demostrar cómo los mecanismos de sincronización permiten coordinar procesos concurrentes y evitar problemas relacionados con el acceso simultáneo a recursos compartidos.

## Objetivo

Implementar una solución concurrente que permita:

* Simular la generación de datos provenientes de sensores de tráfico.
* Procesar los datos mediante un módulo consumidor.
* Utilizar un búfer compartido.
* Aplicar semáforos para controlar la disponibilidad de espacios y datos.
* Utilizar exclusión mutua para proteger el acceso al búfer.
* Prevenir condiciones de carrera y pérdida de información.

## Escenario SIGET

La simulación utiliza tres hilos que trabajan de forma concurrente:

| Hilo       | Función                     |
| ---------- | --------------------------- |
| Sensor 1   | Produce datos de tráfico    |
| Sensor 2   | Produce datos de tráfico    |
| Analizador | Consume y procesa los datos |

Los sensores generan información relacionada con la cantidad de vehículos detectados, mientras que el analizador procesa la información almacenada en el búfer.

## Búfer compartido

El sistema utiliza un búfer con capacidad máxima de **5 datos**.

Los productores agregan información al búfer y el consumidor retira los datos en el mismo orden en que fueron almacenados.

Ejemplo:

```text
Sensor 1 -> Produciendo: 38 vehículos
Búfer -> [38]

Sensor 2 -> Produciendo: 94 vehículos
Búfer -> [38, 94]

Analizador -> Consumiendo dato de Sensor 1: 38 vehículos
Búfer -> [94]
```

Cuando el búfer alcanza su capacidad máxima, los productores deben esperar hasta que el consumidor libere un espacio.

```text
Sensor 1 -> Búfer lleno, esperando espacio...
```

## Mecanismos de concurrencia

### Semáforos

Se utilizan dos semáforos:

* `espacios_disponibles`: controla la cantidad de espacios libres en el búfer.
* `datos_disponibles`: controla la cantidad de datos disponibles para ser consumidos.

Estos mecanismos permiten sincronizar productores y consumidores.

### Exclusión mutua

Se utiliza `threading.Lock()` para garantizar que solamente un hilo pueda modificar el búfer al mismo tiempo.

Esto evita condiciones de carrera cuando varios sensores intentan agregar información simultáneamente o cuando el analizador retira datos.

## Tecnologías utilizadas

* **Python 3**
* Módulo `threading`
* Semáforos
* Exclusión mutua mediante `Lock`
* Programación concurrente

## Ejecución

### Requisitos

Tener instalado **Python 3**.

### Ejecutar el programa

Desde la carpeta del proyecto:

```bash
python productor_consumidor_siget.py
```

También puede ejecutarse directamente desde Visual Studio Code.

## Ejemplo de ejecución

```text
==============================================
     PRODUCTOR - CONSUMIDOR SIGET
==============================================

Sensor 1 -> Produciendo: 38 vehículos
Búfer -> [38]

Sensor 2 -> Produciendo: 94 vehículos
Búfer -> [38, 94]

Analizador -> Consumiendo dato de Sensor 1: 38 vehículos
Búfer -> [94]

Sensor 1 -> Produciendo: 83 vehículos
Búfer -> [94, 83]

...

Búfer -> []

==============================================
       SIMULACIÓN FINALIZADA
==============================================
```

La ejecución demuestra que los productores y el consumidor trabajan de manera concurrente y que los datos son almacenados y procesados correctamente.

## Prevención de problemas de concurrencia

La solución implementa mecanismos de sincronización para evitar:

* Condiciones de carrera.
* Acceso simultáneo no controlado al búfer.
* Inserción de datos cuando el búfer está lleno.
* Consumo de datos cuando el búfer está vacío.
* Pérdida de información durante la comunicación entre productores y consumidor.

## Conclusión

La simulación permite observar de forma práctica el funcionamiento del modelo Productor-Consumidor aplicado a un escenario de tráfico inteligente.

El uso de **semáforos** permite coordinar la disponibilidad de espacios y datos, mientras que la **exclusión mutua** protege el acceso al búfer compartido.

Esta estrategia permite gestionar de manera segura la información generada por los sensores y procesada por el módulo de análisis, contribuyendo a la confiabilidad de un sistema crítico como el SIGET.

## Autor

**Estiven Jaramillo**

Tecnólogo en Desarrollo de Software y Sistemas

