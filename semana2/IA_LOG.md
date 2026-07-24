# Bitácora de IA - Semana 2

Durante esta semana utilicé herramientas de inteligencia artificial como apoyo para organizar las ideas, revisar posibles soluciones, entender errores y mejorar la estructura del proyecto.
La IA no se utilizó para reemplazar todo el trabajo de programación. La utilicé como una herramienta de apoyo para pensar las soluciones, generar propuestas iniciales y entender los errores que iban apareciendo. Después revisé, adapté y probé el código hasta comprobar que funcionara correctamente.



# Entrada 1 - Organización del proyecto

## Situación

Al comenzar la Semana 2 necesitaba organizar el trabajo del sistema de monitoreo IoT para una bodega industrial.

El sistema debía trabajar con 10 sensores de temperatura y humedad, tomar lecturas cada 30 segundos, detectar anomalías cuando la temperatura superara los 35 °C o la humedad superara el 80 %, y generar alertas.

### Pregunta realizada a la IA

Le pedí a la IA que me ayudara a convertir los requisitos del proyecto en historias de usuario y a organizarlas utilizando la técnica MoSCoW.

También le pedí que cada historia tuviera criterios de aceptación verificables utilizando Gherkin y una estimación de Story Points.

### Propuesta de la IA

La IA propuso dividir el sistema en diferentes funcionalidades, comenzando por las partes principales del núcleo:

- Registrar lecturas de sensores.
- Validar los datos recibidos.
- Detectar anomalías de temperatura.
- Detectar anomalías de humedad.
- Configurar los límites de detección.
- Generar alertas.
- Mostrar alertas en consola.
- Guardar alertas en archivos.
- Trabajar con los 10 sensores.
- Realizar lecturas periódicas.
- Simular sensores.
- Realizar pruebas de integración.
- Consultar el historial de alertas.
- Identificar el tipo de anomalía.

### Qué hice con la propuesta

Revisé las historias y las adapté al contexto de mi proyecto.

También agregué criterios Gherkin más concretos para que las historias pudieran comprobarse mediante pruebas.

Después organicé las historias según su importancia utilizando:

- Must.
- Should.
- Could.
- Won't.

Esto me ayudó a definir primero el núcleo del sistema y dejar las funcionalidades adicionales para después.

# Resultado

Terminé con un Product Backlog de 14 historias de usuario.

La principal conclusión fue que antes de intentar trabajar con los 10 sensores completos necesitaba tener funcionando correctamente las piezas principales del sistema: las lecturas, la detección de anomalías y las alertas.



## Entrada 2 - Diseño de SensorReading y trabajo con TDD

### Situación

La primera parte del núcleo que necesitaba implementar era una forma de representar las lecturas de los sensores.

Cada lectura debía tener un identificador de sensor, temperatura, humedad y una marca de tiempo.

También necesitaba evitar que se pudieran crear lecturas con datos inválidos.

### Pregunta o solicitud realizada a la IA

Le pedí a la IA que me ayudara a definir cómo podía representar una lectura de sensor y qué validaciones serían necesarias.

También le pedí ayuda para plantear los tests siguiendo una idea de TDD.

### Propuesta de la IA

La propuesta fue utilizar una `dataclass` inmutable para representar la lectura.

La clase tendría:

- `sensor_id`
- `temperature`
- `humidity`
- `timestamp`

También se propuso validar:

- Que el identificador del sensor no estuviera vacío.
- Que la temperatura estuviera dentro de un rango razonable.
- Que la humedad estuviera entre 0 y 100.

Para TDD, primero se plantearon pruebas para comprobar el comportamiento esperado y después se implementó la clase.

### Qué hice con la propuesta

Adapté la propuesta al proyecto y creé `SensorReading` utilizando:

`@dataclass(frozen=True)`

Después agregué los tests para comprobar tanto los casos correctos como los casos inválidos.

Los tests comprobaron que:

- Una lectura válida se crea correctamente.
- No se permite un identificador vacío.
- No se permite una humedad inválida.
- No se permite una temperatura fuera del rango establecido.
- La lectura es inmutable.

### Resultado

Los tests de `SensorReading` terminaron pasando correctamente.

Esto me permitió tener una estructura confiable para utilizar como entrada en las siguientes partes del sistema.

También pude comprobar la utilidad de TDD porque los tests definieron claramente qué comportamiento esperaba antes de terminar la implementación.

---

## Entrada 3 - Diseño de AnomalyDetector con umbrales inyectados

#Situación

Después de tener las lecturas, necesitaba implementar la lógica para detectar anomalías.

El requisito indicaba que debía detectar una anomalía cuando:

- La temperatura fuera mayor a 35 °C.
- La humedad fuera mayor a 80 %.

También quería evitar que esos valores estuvieran escritos directamente dentro del detector.

### Pregunta o solicitud realizada a la IA

Le pedí a la IA una propuesta para implementar el detector utilizando umbrales configurables e inyectados desde afuera.

### Propuesta de la IA

La propuesta fue crear una estructura llamada `AnomalyThresholds` que almacenara:

- `max_temperature`
- `max_humidity`

Después, `AnomalyDetector` recibiría esos límites desde su constructor.

De esta forma, el detector no tendría que conocer directamente cuáles son los valores de configuración.

También se propuso separar dos responsabilidades:

- `is_anomalous()` para saber si existe una anomalía.
- `reasons()` para conocer si la anomalía fue causada por temperatura, humedad o ambas.

### Qué hice con la propuesta

Implementé el detector utilizando la inyección de dependencias para los umbrales.

Después escribí tests para comprobar:

- Temperatura superior al límite.
- Humedad superior al límite.
- Lectura dentro de los límites.
- Uso de límites personalizados.

También comprobé que los valores de los límites no estuvieran hardcodeados dentro de la lógica principal del detector.

### Resultado

El detector quedó funcionando correctamente y los tests pasaron.

Esta parte fue importante porque permitió que las reglas del sistema fueran configurables y no dependieran directamente de valores escritos dentro de la clase.




## Entrada  - Extensión de Distinción: 10 sensores y prueba de integración

### Situación

Para intentar alcanzar la extensión de Distinción necesitaba agregar un simulador capaz de representar los 10 sensores de la bodega.

Además, debía realizar una prueba de integración que procesara 10 sensores durante 60 ciclos y comprobara que se generaran alertas cuando aparecieran anomalías.

# Pregunta o solicitud realizada a la IA

Le pedí a la IA que me ayudara a diseñar un simulador de sensores que pudiera generar datos realistas utilizando una distribución gaussiana.

También pedí ayuda para que el diseño tuviera conexion adecuada con los primeros codigos echos:

`SensorSimulator`

con:

`SensorReading`

`AnomalyDetector`

y:

`AlertManager`

### Propuesta de la IA

La propuesta fue crear `SensorSimulator` con una cantidad configurable de sensores y utilizar `Random.gauss()` para generar valores de temperatura y humedad.

El simulador debía generar identificadores como:

- `SENSOR-01`
- `SENSOR-02`
- `SENSOR-03`

y continuar hasta:

- `SENSOR-10`

También se propuso generar 60 ciclos de lecturas.

Esto significaría:

10 sensores × 60 ciclos = 600 lecturas.

### Qué hice con la propuesta

Implementé el simulador y configuré la prueba con:

- 10 sensores.
- 60 ciclos.
- Distribución gaussiana para temperatura.
- Distribución gaussiana para humedad.
- Umbral de temperatura de 35 °C.
- Umbral de humedad de 80 %.

También utilicé una semilla (`seed`) para que las pruebas fueran reproducibles.

Durante la integración aparecieron errores porque la forma en la que se llamaba a `AlertManager.send_alert()` no coincidía con los parámetros que esperaba el método.

Revisé el error, ajusté la llamada y utilicé las razones obtenidas por `AnomalyDetector`.

Después de realizar las correcciones volví a ejecutar toda la suite.

### Resultado

Finalmente conseguí que todas las pruebas pasaran:

- 19 tests ejecutados.
- 19 tests pasando.
- 0 tests fallando.
- 99 % de cobertura total ya que en `AnomalyDetector` seguia un pequeño error.

La prueba de integración comprobó que se procesaran las 600 lecturas correspondientes a los 10 sensores durante 60 ciclos y que se generaran alertas para las anomalías encontradas.

Esta parte fue especialmente útil porque permitió comprobar que los componentes no solo funcionaban de manera individual, sino también cuando se conectaban entre sí.


## Reflexión final sobre el uso de IA

Durante esta semana la IA fue una herramienta de apoyo durante todo el proceso, principalmente para pensar la estructura del sistema y asi que el sistema primero tendria funcionalidad antes de ingresar los 10 sensores, revisar alternativas de implementación, entender errores y proponer formas de organizar los tests.

No tomé todas las propuestas de forma automática. En varios momentos tuve que adaptar el código a la estructura real del proyecto y corregir errores que aparecieron al ejecutar las pruebas.

Uno de los aprendizajes más importantes fue que una propuesta de código puede parecer correcta de forma aislada, pero al integrarla con el resto del proyecto pueden aparecer problemas de interfaces, imports o tipos de datos y es ahi donde la IA solo llega a ser una herramienta ya que en si uno es el que tienela idea y la menera de hacer las ejecuciones o la arquitectura del proyecto.

Por eso considero que la parte más importante del uso de IA fue utilizarla como apoyo para analizar los problemas y después comprobar las soluciones ejecutando los tests.

Al final, el resultado fue un sistema con un núcleo funcional, pruebas automatizadas, cobertura superior al 80 % y una extensión capaz de simular 10 sensores durante 60 ciclos.