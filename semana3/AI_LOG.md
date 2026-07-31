# AI_LOG.md

## Entrada 1

**Fecha:** 28/07/2026

**Objetivo**
Diseñar la arquitectura del proyecto antes de comenzar a programar.

**Consulta realizada**
Le pregunté a la IA cuál era la mejor forma de organizar una API con FastAPI siguiendo una arquitectura en capas.

**Respuesta de la IA**
Me recomendó separar el proyecto en routers, services, repositories, models y schemas para mantener cada responsabilidad aislada y facilitar el mantenimiento del código.

**Decisión tomada**
Utilicé esa estructura desde el inicio del proyecto.

**Resultado**
La API quedó organizada por capas y fue mucho más sencillo implementar el CRUD y agregar nuevas funcionalidades.

---

## Entrada 2

**Fecha:** 29/07/2026

**Objetivo**
Implementar las validaciones de sensores y lecturas.

**Consulta realizada**
Le pregunté a la IA cómo dividir correctamente las validaciones entre Pydantic y la lógica de negocio.

**Respuesta de la IA**
Me explicó que Pydantic debía validar la estructura de los datos (tipos, campos obligatorios y unidades permitidas) mientras que las reglas físicas, como rangos de temperatura o humedad, debían implementarse en la capa de servicios.

**Decisión tomada**
Implementé las validaciones de formato en los schemas y las validaciones físicas en ReadingService.

**Resultado**
La API rechaza datos inválidos utilizando los códigos de respuesta correspondientes.

---

## Entrada 3

**Fecha:** 31/07/2026

**Objetivo**
Construir pruebas de integración para verificar el funcionamiento de la API.

**Consulta realizada**
Solicité apoyo para crear pruebas utilizando TestClient de FastAPI y una base de datos temporal.

**Respuesta de la IA**
Me recomendó utilizar SQLite como base de datos de pruebas, sobrescribir la dependencia get_db() y limpiar la base antes de cada prueba para evitar conflictos.

**Decisión tomada**
Implementé una base temporal y desarrollé pruebas para sensores y lecturas.

**Resultado**
Se obtuvo una cobertura superior al 80% y todas las pruebas se ejecutan correctamente.

---

## Entrada 4

**Fecha:** 31/07/2026

**Objetivo**
Corregir errores encontrados durante el desarrollo.

**Consulta realizada**
Consulté varios errores relacionados con SQLAlchemy, dependencias entre capas, mypy y la configuración de los repositorios.

**Respuesta de la IA**
Me ayudó a interpretar los mensajes de error, identificar el origen del problema y ajustar la implementación sin modificar la arquitectura del proyecto.

**Decisión tomada**
Corregí la comunicación entre routers, servicios y repositorios, además de revisar las configuraciones necesarias para Ruff y mypy.

**Resultado**
El proyecto quedó funcionando correctamente, con Swagger disponible en `/docs`, Ruff sin observaciones, mypy limpio y todas las pruebas aprobadas.