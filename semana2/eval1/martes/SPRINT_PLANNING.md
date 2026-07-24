# Sprint  Planning de la  Semana 2


Mi objetivo para este sprint es construir el núcleo básico del sistema de monitoreo IoT.

Al terminar el sprint quiero tener una base funcional donde pueda:

- Crear lecturas de temperatura y humedad.
- Validar que las lecturas sean correctas.
- Detectar anomalías de temperatura y humedad.
- Configurar los límites de las anomalías sin tener que modificar directamente el código del detector.
- Generar y enviar alertas cuando se detecte una anomalía.
- Enviar las alertas a diferentes destinos utilizando estrategias intercambiables.

La idea es que al terminar este sprint ya tenga funcionando la parte más importante del sistema.

Todavía no voy a trabajar en la simulación de los 10 sensores ni en la prueba de integración de 60 ciclos, porque primero quiero asegurarme de que el núcleo del sistema funcione correctamente.



# Historias seleccionadas para el Sprint 1

## US01 - Registrar una lectura de un sensor

**Story Points:** 3  
**Prioridad:** Must

Seleccioné esta historia porque todo el sistema depende de tener una forma clara de representar una lectura de temperatura y humedad.

# Tareas

- Crear la clase `SensorReading` - 1 h
- Definir los atributos de la lectura - 1 h
- Agregar validación de los datos - 1 h
- Crear tests con TDD - 1 h

**Total:** 4 horas



## US02 - Validar los datos de una lectura

**Story Points:** 3  
**Prioridad:** Must

Seleccioné esta historia porque no quiero que el resto del sistema trabaje con datos inválidos.

## Tareas

- Definir las reglas de validación - 1 h
- Validar que el identificador del sensor no esté vacío - 1 h
- Validar los rangos de temperatura y humedad - 1 h
- Crear y ejecutar tests para datos inválidos - 1 h

**Total:** 4 horas


## US03 - Detectar temperatura fuera del límite

**Story Points:** 3  
*Prioridad:** Must

Seleccioné esta historia porque detectar temperaturas demasiado altas es una de las funciones principales del sistema de monitoreo.

### Tareas

- Crear la clase `AnomalyDetector` - 1 h
- Crear la configuración `AnomalyThresholds` - 1 h
- Implementar la detección de temperatura por encima del límite - 1 h
- Crear tests con TDD - 1 h

**Total:** 4 horas



## US04 - Detectar humedad fuera del límite

**Story Points:** 3  
**Prioridad:** Must

Seleccioné esta historia porque una humedad demasiado alta también puede afectar los productos almacenados en la bodega.

### Tareas

- Agregar el umbral máximo de humedad - 1 h
- Implementar la detección de humedad alta - 1 h
- Crear tests para humedad normal y anormal - 1 h
- Comprobar el comportamiento cuando temperatura y humedad superan los límites - 1 h

**Total:** 4 horas



# US06 - Generar una alerta cuando exista una anomalía

**Story Points:** 5  
**Prioridad:* Must

Seleccioné esta historia porque detectar una anomalía no es suficiente si el sistema no puede informar que existe un problema.

### Tareas

- Definir una estrategia abstracta para enviar alertas - 1 h
- Crear la estrategia de alerta por consola - 1 h
- Crear la estrategia de alerta por archivo - 1 h
- Crear `AlertManager` y conectarlo con las estrategias - 1 h

**Total:** 4 horas



## US14 - Mantener las estrategias de alerta intercambiables

**Story Points:** 3  
**Prioridad:** Should

Seleccioné esta historia porque quiero que el sistema pueda cambiar la forma de enviar alertas sin tener que modificar la lógica principal de `AlertManager`.

Esto me permite utilizar una estrategia para consola y otra para archivo, y en el futuro podría agregar nuevas estrategias sin cambiar el funcionamiento principal.

### Tareas

- Crear la abstracción `AlertStrategy` - 1 h
- Implementar `ConsoleAlertStrategy` - 1 h
- Implementar `FileAlertStrategy` - 1 h
- Crear tests para comprobar el uso de diferentes estrategias - 1 h

**Total:** 4 horas



# Resumen del Sprint

| Historia | Story Points | Prioridad | Horas estimadas |
|---|---:|---|---:|
| US01 - Registrar una lectura | 3 | Must | 4 h |
| US02 - Validar una lectura | 3 | Must | 4 h |
| US03 - Detectar temperatura | 3 | Must | 4 h |
| US04 - Detectar humedad | 3 | Must | 4 h |
| US06 - Generar alertas | 5 | Must | 4 h |
| US14 - Estrategias de alerta intercambiables | 3 | Should | 4 h |

**Total:** 20 Story Points

**Tiempo estimado de tareas:** 24 horas, suponiendo que en cada tarea me lleve 4 horas en completarla



# porque de cada selección

Seleccioné estas seis historias porque juntas forman el núcleo principal del sistema.

Primero necesito una estructura para representar las lecturas. Por eso comienzo con `SensorReading`.

Después necesito asegurarme de que los datos que recibe el sistema sean válidos. Por eso agrego las validaciones antes de continuar con el procesamiento.

Una vez que tengo lecturas válidas, necesito analizarlas. Para eso utilizo `AnomalyDetector`, que permite detectar problemas tanto de temperatura como de humedad.

También decidí que los límites no deben estar escritos directamente dentro del detector. Por eso utilizo `AnomalyThresholds`, que permite configurar los valores desde afuera.

Finalmente necesito informar cuando se encuentra una anomalía. Para eso utilizo `AlertManager` junto con diferentes estrategias de alerta.

La selección de estas historias también me permite aplicar principios de diseño que ya trabajé anteriormente, especialmente la separación de responsabilidades y la posibilidad de cambiar implementaciones sin modificar la lógica principal.

Las historias relacionadas con los 10 sensores simulados y los 60 ciclos quedan fuera de este sprint porque las considero parte de la extensión de la Distinción. Primero quiero tener el núcleo funcionando y probado antes de utilizarlo en una prueba de integración más grande.


# Orden en el que voy a trabajar

Voy a trabajar en el siguiente orden:

1. Crear `SensorReading`.
2. Escribir los primeros tests y validar los datos de las lecturas.
3. Crear `AnomalyThresholds`.
4. Crear `AnomalyDetector`.
5. Agregar la detección de temperatura y humedad.
6. Crear la abstracción para las estrategias de alerta.
7. Implementar `ConsoleAlertStrategy`.
8. Implementar `FileAlertStrategy`.
9. Crear `AlertManager`.
10. Ejecutar todos los tests y revisar la cobertura.

La idea es desarrollar cada parte utilizando TDD:

1. Primero escribo el test.
2. Ejecuto el test y compruebo que falle.
3. Escribo el código mínimo necesario para que pase.
4. Ejecuto nuevamente los tests.
5. Refactorizo el código si hace falta.
6. Vuelvo a ejecutar los tests para comprobar que todo siga funcionando.

De esta forma, no estoy escribiendo todo el código primero y probándolo al final. Voy construyendo cada parte acompañada de sus pruebas.



# Definition of Done

Para considerar una historia como terminada, voy a comprobar que:

- [ ] El código de la funcionalidad está implementado.
- [ ] Los tests correspondientes están escritos.
- [ ] Los tests pasan correctamente.
- [ ] La funcionalidad cumple los criterios Gherkin definidos en el Product Backlog.
- [ ] No existen errores en `pytest`.
- [ ] La cobertura del código principal es de al menos 80%.
- [ ] El código pasa `ruff check`.
- [ ] El código pasa `mypy`.
- [ ] Las tareas de la historia están terminadas.
- [ ] La implementación está integrada con el resto del sistema.
- [ ] El código está guardado en Git.
- [ ] El commit tiene un mensaje claro.
- [ ] La funcionalidad se puede explicar fácilmente.
- [ ] El código no contiene errores conocidos pendientes de corregir.


# Resultado esperado del Sprint

Al terminar este sprint espero tener funcionando las tres piezas principales del sistema:

`SensorReading` → representa y valida las lecturas de los sensores.

`AnomalyDetector` → revisa las lecturas y detecta anomalías utilizando límites configurables.

`AlertManager` → gestiona el envío de alertas utilizando diferentes estrategias, como consola o archivo.

Con estas tres piezas tendré una base sólida para continuar con la siguiente parte del proyecto.

En la extensión de la Distinción podré utilizar este núcleo para trabajar con un simulador de 10 sensores, generar lecturas durante 60 ciclos y comprobar mediante una prueba de integración que las lecturas anormales terminan generando las alertas correspondientes.