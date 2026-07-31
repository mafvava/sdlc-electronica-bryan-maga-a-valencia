# SensorHub-API

API REST desarrollada con FastAPI para administrar sensores y sus lecturas. El proyecto implementa una arquitectura en capas, persistencia con SQLAlchemy, validaciones mediante Pydantic y pruebas de integración.


## Tecnologías utilizadas

- Python 3.12
- FastAPI
- SQLAlchemy 2.x
- SQLite
- Pydantic
- Uvicorn
- Pytest
- Ruff
- MyPy


## Estructura del proyecto

aqui en este apartado seguimos la arquitectura propuesta, aunque estaba dentro de la carpeta semana 3 esa solo quedo como evidencia de seguimiento.
app/
├── main.py
├── database.py
├── models/
├── repositories/
├── routers/
├── schemas/
└── services/

tests/
docs/
AI_LOG.md
README.md
requirements.txt


## Arquitectura

El proyecto sigue una arquitectura de cuatro capas:


Router
   ↓
Service
   ↓
Repository
   ↓
Model (Base de Datos)

Cada capa tiene una responsabilidad específica:

- **Routers:** reciben las solicitudes HTTP.
- **Services:** contienen la lógica de negocio.
- **Repositories:** realizan el acceso a la base de datos.
- **Models:** representan las tablas mediante SQLAlchemy.


## Instalación

Clonar el repositorio:


git clone <URL_DEL_REPOSITORIO>


Entrar al proyecto:


cd semana3 (pero una ves echa la modificacion propuesta ya solo queso dentro de la raiz)


Crear entorno virtual:


python -m venv .venv


Activar entorno virtual:

### Windows

.venv\Scripts\activate


Instalar dependencias:

pip install -r requirements.txt



## Ejecutar la API

uvicorn app.main:app --reload


La API estará disponible en:


http://127.0.0.1:8000



## Swagger

Documentación automática:


http://127.0.0.1:8000/docs


## Endpoints principales

### Sensores

- GET /sensors
- GET /sensors/{id}
- POST /sensors
- PUT /sensors/{id}
- DELETE /sensors/{id}

### Lecturas

- GET /readings
- GET /readings/{id}
- POST /readings
- DELETE /readings/{id}
- GET /readings/filter/date


## Funcionalidades

- CRUD completo de sensores.
- CRUD completo de lecturas.
- Arquitectura en cuatro capas.
- Validaciones mediante Pydantic.
- Validación física de temperatura y humedad.
- Prevención de sensores duplicados.
- Paginación.
- Filtro por rango de fechas.
- Swagger automático.
- Pruebas de integración.
- Cobertura superior al 80%.


## Ejecutar pruebas


python -m pytest -v


Cobertura:


python -m pytest --cov=app --cov-report=term-missing



## Análisis estático

Ruff


python -m ruff check app tests


MyPy


python -m mypy app



## Autor

Bryan Magaña Valencia

Proyecto desarrollado para la materia de Desarrollo de Software (EDSIA).

## Actualización posterior a la revisión por pares

Se realizaron ajustes menores en la documentación y organización del proyecto después del peer review.git add README.md
