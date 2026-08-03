# analisis realizados con IA para el codigo

## Entrada 1


**Objetivo**

Quería organizar el proyecto siguiendo la arquitectura en cuatro capas que se pedía para SensorHub. Mi duda era cómo dividir correctamente la lógica entre routers, services, repositories y models sin repetir código ni mezclar responsabilidades queriendo seguir las arquitecturas de la semana 2 y 1.

**Consulta realizada a la IA**

Le pedí una explicación sobre cómo estructurar el proyecto y cómo debía comunicarse cada capa con la siguiente.

**Respuestas útil**

La IA me explicó que los routers únicamente reciben las solicitudes HTTP, los services contienen toda la lógica de negocio, los repositories son los encargados de acceder a la base de datos y los models representan las tablas. También me mostró cómo inyectar la sesión de la base de datos desde los routers hacia los servicios.

**Qué hice con esa respuesta**

Reorganicé todo el proyecto respetando esa arquitectura y moví la lógica correspondiente a cada capa. Al finalizar, el código quedó más limpio y fue mucho más sencillo localizar los errores cuando aparecieron y tomando en cuenta que esta semana iba a quedar dentro de la raiz, usea la carpeta semana 3 para evidencias de pruebas y test.

**Reflexión**

Entendí que separar responsabilidades hace que el proyecto sea más fácil de mantener y de escalar. Antes tendía a colocar toda la lógica en un solo archivo y ahora veo por qué esa práctica no es recomendable.

---

## Entrada 2


**Objetivo**

Necesitaba corregir varios errores que aparecieron al ejecutar MyPy después de modificar los repositorios y los servicios.

**Consulta realizada a la IA**

Le mostré los errores que aparecían en la terminal y le pedí ayuda para identificar cuál era el origen del problema.

**Respuesta útil**

La IA detectó que algunos métodos de los repositorios ya no coincidían con la forma en la que los servicios los estaban utilizando. También encontró problemas de indentación y diferencias en los parámetros de varios métodos.

**Qué hice con esa respuesta**

Actualicé los repositorios y los servicios para que utilizaran la misma estructura de parámetros y corregí la indentación de algunos métodos. Después de esos cambios, MyPy dejó de mostrar errores y todas las pruebas siguieron funcionando correctamente.

**Reflexión**

Aprendí que MyPy ayuda a encontrar errores antes de ejecutar el programa y que mantener consistencia entre las capas evita muchos problemas durante el desarrollo.


## Entrada 3


**Objetivo**

Quería comprobar que la API realmente funcionaba y no solamente compilara correctamente.

**Consulta realizada a la IA**

Le pedí ayuda para crear pruebas de integración utilizando FastAPI TestClient y organizar correctamente los archivos de pruebas.

**Respuesta útil**

La IA me ayudó a configurar una base de datos SQLite temporal para las pruebas, crear un cliente de pruebas y escribir casos para crear, consultar, actualizar y eliminar sensores y lecturas.

**Qué hice con esa respuesta**

Implementé los archivos de pruebas, ejecuté Pytest, corregí algunos errores relacionados con la base de datos y finalmente obtuve todas las pruebas aprobadas con una cobertura superior al 94%.

**Reflexión**

Comprobé que las pruebas no solo sirven para cumplir un requisito, sino que también ayudan a detectar errores rápidamente cuando se modifica el código y aunque aparecias varios errores, siempre se iban mas a un solo documento mal realizado.



## Entrada 4


**Objetivo**

Quería mejorar la calidad de la API evitando que existieran sensores duplicados con el mismo nombre.

**Consulta realizada a la IA**

Le pregunté cuál era la mejor forma de validar nombres repetidos siguiendo una arquitectura limpia y utilizando los códigos HTTP adecuados.

**Respuesta útil**

La IA propuso agregar una búsqueda por nombre dentro del repositorio y realizar la validación desde la capa de servicio. Si el nombre ya existía, la API debía responder con un código 409 Conflict.

**Qué hice con esa respuesta**

Agregué el método get_by_name() en el repositorio, incorporé la validación en el servicio y escribí una prueba adicional para verificar que el comportamiento fuera correcto. Todas las pruebas continuaron pasando después del cambio.

Reflexión

Aprendí que una API no solo debe funcionar, sino también proteger la integridad de los datos y responder utilizando los códigos HTTP apropiados.
