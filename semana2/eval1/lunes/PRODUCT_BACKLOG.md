# Product Backlog - Semana 2

En esta semana estoy trabajando en un sistema de monitoreo IoT pensado para una bodega industrial.

La idea principal del sistema es trabajar con sensores de temperatura y humedad. El sistema debe recibir las lecturas de los sensores, revisar si alguno de los valores está fuera de los límites permitidos y generar una alerta cuando encuentre una anomalía.

El escenario que estoy considerando es una bodega con 10 sensores, donde cada sensor puede generar lecturas periódicas. Para las pruebas y la extensión de la Distinción también voy a utilizar un simulador que me permite probar el comportamiento de los 10 sensores durante 60 ciclos sin depender de sensores físicos reales.

Como soy el único desarrollador del proyecto, voy a priorizar primero las funciones que forman el núcleo del sistema. Mi idea es construir primero algo pequeño pero funcional y después agregar las mejoras.

Para ordenar las prioridades voy a utilizar MoSCoW:

- **Must:** Lo necesito sí o sí para que el núcleo del sistema funcione.
- **Should:** Es importante y mejora el sistema, pero puede funcionar sin esto inicialmente.
- **Could:** Me gustaría agregarlo como una mejora cuando el núcleo ya esté funcionando.
- **Won't:** Por ahora no forma parte del alcance de este sprint.


 01 - Registrar una lectura de un sensor

Como operador de la bodega,  
quiero registrar una lectura de temperatura y humedad junto con el identificador del sensor,  
para saber qué valores está enviando cada sensor.

Prioridad: Must  
Story Points: 3

 Criterios de aceptación

gherkin
Feature: Registrar lecturas de sensores

  Scenario: Registrar una lectura válida
    Given que tengo un sensor con identificador "S01"
    And la temperatura es de 25.5 grados Celsius
    And la humedad es de 60 por ciento
    When creo una lectura del sensor
    Then la lectura debe conservar el identificador "S01"
    And debe conservar la temperatura de 25.5
    And debe conservar la humedad de 60


02 - Validar los datos de una lectura

Como sistema de monitoreo,
quiero validar que las lecturas recibidas tengan datos correctos,
para evitar trabajar con información inválida.

Prioridad: Must
Story Points: 3

Criterios de aceptación
Feature: Validar lecturas

  Scenario: Rechazar un identificador vacío
    Given que intento crear una lectura
    And el identificador del sensor está vacío
    When creo la lectura
    Then el sistema debe rechazarla

  Scenario: Rechazar una humedad fuera de rango
    Given que intento crear una lectura
    And la humedad es menor que 0
    When creo la lectura
    Then el sistema debe rechazarla

  Scenario: Rechazar una temperatura fuera de rango
    Given que intento crear una lectura
    And la temperatura está fuera del rango permitido
    When creo la lectura
    Then el sistema debe rechazarla


03 - Detectar temperatura fuera del límite

Como operador de la bodega,
quiero detectar cuando la temperatura supere los 35 grados Celsius,
para identificar rápidamente una posible anomalía.

Prioridad: Must
Story Points: 3

Criterios de aceptación
Feature: Detectar temperatura alta

  Scenario: Detectar temperatura por encima del límite
    Given que el límite de temperatura está configurado en 35 grados Celsius
    And recibo una lectura de 36 grados Celsius
    When analizo la lectura
    Then el sistema debe marcarla como anomalía

  Scenario: Aceptar temperatura dentro del límite
    Given que el límite de temperatura está configurado en 35 grados Celsius
    And recibo una lectura de 30 grados Celsius
    When analizo la lectura
    Then el sistema no debe marcarla como anomalía


04 - Detectar humedad fuera del límite

Como operador de la bodega,
quiero detectar cuando la humedad supere el 80 por ciento,
para saber cuándo las condiciones de la bodega pueden representar un problema.

Prioridad: Must
Story Points: 3

Criterios de aceptación
Feature: Detectar humedad alta

  Scenario: Detectar humedad por encima del límite
    Given que el límite de humedad está configurado en 80 por ciento
    And recibo una lectura con 85 por ciento de humedad
    When analizo la lectura
    Then el sistema debe marcarla como anomalía

  Scenario: Aceptar humedad dentro del límite
    Given que el límite de humedad está configurado en 80 por ciento
    And recibo una lectura con 70 por ciento de humedad
    When analizo la lectura
    Then el sistema no debe marcarla como anomalía


05 - Configurar los límites de anomalías

Como desarrollador del sistema,
quiero poder inyectar los límites de temperatura y humedad,
para cambiar las reglas de detección sin tener que modificar directamente el código del detector.

Prioridad: Must
Story Points: 3

Criterios de aceptación
Feature: Configurar límites de anomalías

  Scenario: Usar límites personalizados
    Given que creo un detector con temperatura máxima de 30 grados Celsius
    And humedad máxima de 70 por ciento
    And recibo una lectura de 32 grados Celsius y 60 por ciento de humedad
    When analizo la lectura
    Then el sistema debe detectar una anomalía por temperatura

  Scenario: Usar nuevos límites mediante inyección
    Given que el detector recibe sus límites mediante una configuración externa
    When creo un detector con nuevos valores de temperatura y humedad
    Then el detector debe utilizar esos nuevos límites


06 - Generar una alerta cuando exista una anomalía

Como operador de la bodega,
quiero recibir una alerta cuando se detecte una anomalía,
para poder actuar antes de que el problema afecte a los productos almacenados.

Prioridad: Must
Story Points: 5

Criterios de aceptación
Feature: Generar alertas

  Scenario: Generar alerta por temperatura alta
    Given que una lectura supera el límite de temperatura
    When el sistema detecta la anomalía
    Then debe generar una alerta
    And la alerta debe indicar que la temperatura está fuera del límite

  Scenario: Generar alerta por humedad alta
    Given que una lectura supera el límite de humedad
    When el sistema detecta la anomalía
    Then debe generar una alerta
    And la alerta debe indicar que la humedad está fuera del límite


07 - Mostrar alertas en consola

Como operador de la bodega,
quiero que las alertas puedan mostrarse en consola,
para ver rápidamente cuando ocurre una anomalía durante las pruebas o la operación del sistema.

Prioridad: Should
Story Points: 2

Criterios de aceptación
Feature: Mostrar alertas en consola

  Scenario: Mostrar una alerta en consola
    Given que existe una anomalía detectada
    And está configurada la estrategia de alerta por consola
    When envío la alerta
    Then el mensaje debe aparecer en la salida de consola


08 - Guardar alertas en un archivo

Como operador de la bodega,
quiero guardar las alertas en un archivo,
para tener un registro de los eventos que han ocurrido.

Prioridad: Should
Story Points: 3

Criterios de aceptación
Feature: Guardar alertas en archivo

  Scenario: Guardar una alerta en un archivo
    Given que existe una anomalía detectada
    And está configurada la estrategia de alerta por archivo
    When envío la alerta
    Then el mensaje debe guardarse en el archivo

  Scenario: Mantener varias alertas
    Given que ya existe una alerta guardada
    When envío una segunda alerta
    Then el archivo debe conservar las dos alertas


09 - Monitorear los 10 sensores de la bodega

Como operador de la bodega,
quiero procesar las lecturas de los 10 sensores,
para tener información de todas las áreas importantes de la bodega.

Prioridad: Must
Story Points: 5

Criterios de aceptación
Feature: Monitorear 10 sensores

  Scenario: Procesar una lectura de cada sensor
    Given que existen 10 sensores configurados
    And cada sensor genera una lectura
    When el sistema procesa un ciclo
    Then debe procesar 10 lecturas
    And cada lectura debe estar asociada a su sensor correspondiente

  Scenario: Identificar el sensor con anomalía
    Given que uno de los 10 sensores genera una lectura fuera de los límites
    When el sistema procesa el ciclo
    Then debe identificar el sensor que generó la anomalía


10 - Procesar ciclos de monitoreo

Como operador de la bodega,
quiero que el sistema pueda procesar ciclos consecutivos de lecturas,
para mantener actualizado el estado de los sensores.

Prioridad: Must
Story Points: 5

Criterios de aceptación
Feature: Procesar ciclos de monitoreo

  Scenario: Procesar un ciclo completo
    Given que existen 10 sensores configurados
    When el sistema ejecuta un ciclo de monitoreo
    Then debe procesar una lectura de cada sensor

  Scenario: Procesar varios ciclos consecutivos
    Given que existen 10 sensores configurados
    When el sistema ejecuta 60 ciclos de monitoreo
    Then debe procesar 600 lecturas en total
    And cada ciclo debe contener lecturas de los 10 sensores


11 - Simular sensores para pruebas

Como desarrollador,
quiero poder simular lecturas de temperatura y humedad,
para probar el sistema sin depender de sensores físicos reales.

Prioridad: Could
Story Points: 5

Criterios de aceptación
Feature: Simular lecturas de sensores

  Scenario: Generar lecturas para 10 sensores
    Given que el simulador está configurado para trabajar con 10 sensores
    When genero un ciclo de lecturas
    Then debe generar 10 lecturas
    And cada lectura debe tener un identificador de sensor diferente

  Scenario: Generar valores con distribución gaussiana
    Given que el simulador está configurado con una media y desviación estándar
    When genero varias lecturas
    Then los valores deben variar entre ciclos
    And los valores deben generarse utilizando una distribución gaussiana

  Scenario: Repetir resultados usando una semilla
    Given que el simulador utiliza una semilla determinada
    When genero las mismas lecturas nuevamente con la misma semilla
    Then los resultados deben poder reproducirse


12 - Ejecutar una prueba de integración con 10 sensores

Como desarrollador,
quiero probar el sistema completo con 10 sensores simulados durante 60 ciclos,
para comprobar que la detección de anomalías y las alertas funcionan juntas.

Prioridad: Could
Story Points: 5

Criterios de aceptación
Feature: Probar el monitoreo completo

  Scenario: Procesar 10 sensores durante 60 ciclos
    Given que tengo 10 sensores simulados
    And el sistema está configurado para detectar anomalías
    When ejecuto 60 ciclos de lectura
    Then el sistema debe procesar 600 lecturas
    And debe detectar las lecturas que superen los límites
    And debe generar alertas para las anomalías detectadas

  Scenario: Guardar las alertas generadas
    Given que se detectan anomalías durante los 60 ciclos
    And está configurada la estrategia de alertas por archivo
    When termina la prueba de integración
    Then el archivo debe contener una alerta por cada anomalía detectada


13 - Identificar el tipo de anomalía

Como operador de la bodega,
quiero saber si una alerta fue causada por temperatura o humedad,
para entender rápidamente cuál es el problema.

Prioridad: Should
Story Points: 3

Criterios de aceptación
Feature: Identificar tipo de anomalía

  Scenario: Identificar anomalía de temperatura
    Given que una lectura supera el límite de temperatura
    And la humedad está dentro del límite
    When el sistema analiza la lectura
    Then debe identificar "temperature" como razón de la anomalía

  Scenario: Identificar anomalía de humedad
    Given que una lectura supera el límite de humedad
    And la temperatura está dentro del límite
    When el sistema analiza la lectura
    Then debe identificar "humidity" como razón de la anomalía

  Scenario: Identificar múltiples razones
    Given que una lectura supera el límite de temperatura
    And también supera el límite de humedad
    When el sistema analiza la lectura
    Then debe identificar ambas razones


14 - Mantener las estrategias de alerta intercambiables

Como desarrollador,
quiero que el sistema pueda cambiar entre diferentes estrategias para enviar alertas,
para poder utilizar consola, archivo u otras estrategias sin modificar el funcionamiento principal del gestor de alertas.

Prioridad: Should
Story Points: 3

Criterios de aceptación
Feature: Usar estrategias de alerta intercambiables

  Scenario: Usar estrategia de consola
    Given que el gestor de alertas recibe una estrategia de consola
    When envío una alerta
    Then la alerta debe mostrarse en consola

  Scenario: Usar estrategia de archivo
    Given que el gestor de alertas recibe una estrategia de archivo
    When envío una alerta
    Then la alerta debe guardarse en un archivo

  Scenario: Cambiar la estrategia
    Given que el gestor de alertas recibe una estrategia mediante inyección
    When cambio la estrategia utilizada
    Then el gestor debe enviar las nuevas alertas utilizando la nueva estrategia
    
Priorización general

En total definí 14 historias de usuario para representar las principales necesidades del sistema.

Must

Las historias que considero indispensables para tener un núcleo funcional son:

Registrar lecturas.
Validar los datos.
Detectar temperaturas fuera del límite.
Detectar humedades fuera del límite.
Configurar los límites mediante inyección.
Generar alertas.
Procesar los 10 sensores.
Procesar varios ciclos de monitoreo.

Estas historias son mi prioridad porque representan el flujo principal del sistema: recibir una lectura, validarla, analizarla y generar una alerta si es necesario.

Should

Como siguientes prioridades tengo:

Mostrar alertas en consola.
Guardar alertas en archivo.
Identificar el tipo de anomalía.
Mantener las estrategias de alerta intercambiables.

Estas funcionalidades hacen que el sistema sea más práctico y fácil de ampliar.

Could

Como mejoras y extensión del proyecto tengo:

Simular sensores mediante una distribución gaussiana.
Ejecutar una prueba de integración con 10 sensores durante 60 ciclos.

Estas historias son especialmente útiles para probar el comportamiento del sistema sin depender de sensores físicos reales.

Won't

Por ahora no voy a implementar dentro del alcance principal:

Conexión directa con sensores físicos.
Un sistema real de temporización de 30 segundos.
Un panel web para visualizar los datos.
Una base de datos para almacenar todas las lecturas.
Notificaciones externas como correo o SMS.

Mi prioridad inicial es construir primero un núcleo pequeño pero funcional. Quiero que el sistema pueda recibir lecturas, validarlas, detectar anomalías y generar alertas.

Después puedo ampliar el sistema para trabajar con los 10 sensores, ejecutar múltiples ciclos y probar todo el flujo mediante el simulador.

Para la extensión de la Distinción, el simulador me permite demostrar el comportamiento del sistema con 10 sensores durante 60 ciclos, generando un total de 600 lecturas y comprobando que las anomalías detectadas terminan generando las alertas correspondientes.

De esta forma, el backlog no solo representa las funcionalidades del sistema, sino también el orden en el que considero más lógico desarrollarlas y probarlas.