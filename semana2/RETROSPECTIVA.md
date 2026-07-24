# Retrospectiva - Semana 2

En este sprint trabajé en la construcción del núcleo principal del sistema de monitoreo IoT para la bodega industrial.

Mi objetivo era conseguir una base funcional que pudiera recibir lecturas de sensores, validar los datos, detectar anomalías y generar alertas.

 ¿Qué salió bien?

Una de las cosas que mejor salió fue organizar el trabajo por partes. Primero trabajé en `SensorReading`, después en `AnomalyDetector` y finalmente en `AlertManager`.

Esto me ayudó a no intentar hacer todo el sistema de una sola vez y a poder probar cada parte por separado.

También me funcionó bien trabajar con TDD. Primero creé los tests para definir qué esperaba que hiciera cada parte del sistema y después fui implementando el código necesario para que los tests pasaran.

Con `SensorReading` pude validar que los datos básicos fueran correctos, como el identificador del sensor, la temperatura y la humedad.

Con `AnomalyDetector` conseguí que los límites de temperatura y humedad fueran configurables. Esto fue importante porque los valores de `35 °C` y `80 %` no quedaron escritos directamente dentro de la lógica de detección, sino que se pueden pasar desde afuera.

También pude implementar `AlertManager` utilizando una estrategia abstracta. De esta forma pude tener una estrategia para mostrar alertas en consola y otra para guardarlas en un archivo.

Otra cosa positiva fue que al final pude integrar las diferentes partes y probar el funcionamiento con 10 sensores simulados durante 60 ciclos. Esto me permitió comprobar que el sistema podía procesar 600 lecturas y generar alertas cuando encontraba anomalías.

Los tests también terminaron funcionando correctamente y la cobertura del código principal quedó por encima del mínimo solicitado.

## ¿Qué fue lo más difícil?

Lo que más se me dificultó fue organizar correctamente la estructura de carpetas y los imports de Python.

Al principio tuve problemas porque los tests no encontraban el paquete `semana2`. El problema estaba relacionado con la forma en la que estaba ejecutando `pytest` y con la estructura de los paquetes.

La solución fue ejecutar los tests usando:

`python -m pytest`

en lugar de ejecutar directamente `pytest`.

También tuve algunos errores durante la prueba de integración. Por ejemplo, inicialmente el método `send_alert()` no recibía los mismos parámetros que se estaban enviando desde el test de integración.

Después de revisar el error, ajusté la integración para que el detector pudiera obtener las razones de la anomalía y que estas fueran enviadas correctamente al sistema de alertas.

Estos errores me ayudaron a entender mejor la importancia de mantener consistentes las interfaces entre las diferentes partes del sistema.

## ¿Qué podría mejorar?

Creo que podría mejorar la planificación inicial del proyecto.

Al principio estaba pensando en las funcionalidades de manera más general, pero al momento de implementarlas tuve que ir definiendo detalles que no había considerado desde el principio.

También podría mejorar la organización de los commits. Para la siguiente semana quiero intentar hacer commits más pequeños y específicos, de manera que cada commit represente un cambio concreto.

Por ejemplo:

- Un commit para `SensorReading`.
- Un commit para `AnomalyDetector`.
- Un commit para `AlertManager`.
- Un commit para la integración de los sensores simulados.
- Un commit para documentación.

Esto haría que el historial de Git sea más fácil de entender y también serviría como evidencia del proceso de desarrollo.

## ¿Qué aprendí?

Aprendí que escribir los tests antes o durante la implementación me ayuda a tener más claro qué debe hacer cada componente.

También entendí mejor la importancia de separar responsabilidades.

`SensorReading` se encarga de representar y validar una lectura.

`AnomalyDetector` se encarga de revisar si una lectura es una anomalía.

`AlertManager` se encarga de gestionar el envío de alertas.

El simulador se encarga de generar datos para poder probar el sistema sin tener que conectar sensores físicos.

Esta separación hace que sea más sencillo probar cada componente y cambiar una parte sin tener que modificar todo el sistema.

También aprendí que las pruebas de integración son diferentes a los tests unitarios. Los tests unitarios me permiten comprobar cada componente por separado, mientras que la prueba de integración me permite comprobar que todos los componentes funcionan correctamente cuando se conectan entre sí.

## Acción concreta para el siguiente sprint

Para el siguiente sprint voy a mejorar la organización del proyecto y voy a crear commits más pequeños y descriptivos.

También voy a intentar definir desde el principio las interfaces que van a utilizar los diferentes componentes para evitar errores de integración como los que tuve con `AlertManager`.

Además, voy a mantener la estrategia de trabajar primero con tests y después implementar la funcionalidad, porque durante este sprint comprobé que TDD me ayudó a detectar errores rápidamente y a tener más confianza en el código.

## Conclusión

En general, considero que el sprint cumplió su objetivo.

Terminé con un núcleo funcional capaz de representar lecturas, detectar anomalías usando límites configurables y generar alertas mediante diferentes estrategias.
Además, pude extender el sistema con un simulador de 10 sensores y una prueba de integración de 60 ciclos.

Aunque tuve algunos problemas con la estructura de los paquetes y la integración entre componentes, pude resolverlos y terminar con todos los tests pasando y una cobertura superior al 80%.

Para el siguiente sprint quiero mantener esta forma de trabajar, pero mejorar principalmente la planificación, la organización de los commits y la definición de las interfaces entre componentes.