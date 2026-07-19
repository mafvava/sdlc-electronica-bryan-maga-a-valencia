# EDSIA — check Semana 1


Este proyecto forma parte de la Semana 1 de EDSIA.

La idea principal de esta semana fue tomar conceptos que normalmente usamos en electrónica, firmware y sistemas embebidos, y llevarlos al mundo del software moderno usando Python.

El proyecto está basado en un dominio sencillo: **sensores industriales de presión**.

No buscamos hacer un sistema industrial completo. La intención es practicar buenas formas de organizar código, probarlo y hacerlo fácil de mantener.

---


Durante esta semana trabajamos en diferentes temas:

 Python moderno y tipado.
 `dataclasses`.
 `Enums`.
 `Protocols`.
 Máquinas de estados.
 Principios SOLID.
 Pruebas automatizadas con `pytest`.
 Análisis de código con `ruff`.
 Verificación de tipos con `mypy`.
 Diseño de un driver UART.
 Parsing de mensajes Modbus y NMEA.
 Persistencia de datos en formato JSON-lines.
 Uso de Git con commits pequeños y descriptivos.
 Registro del uso de inteligencia artificial mediante `AI_LOG.md`.

Todo está organizado por días para poder seguir el avance de la semana de una forma sencilla, aunque cada dia equivale a lo que se mencionaba en classroom, todos los dias trabajan en conjunto uniendolos con un INIT y asi dejar todo el bloque de la semana con cada funcion correspondiente.


La estructura principal de la Semana 1 está organizada de esta manera:

semana1/
│
├── lunes/
│   ├── reading.py
│   └── test_reading.py
│
├── martes/
│   ├── fsm_demo.py
│   └── test_fsm.py
│
├── miercoles/
│   ├── solid_srp_ocp_lsp.py
│   └── test_solid_srp_ocp_lsp.py
│
├── jueves/
│   ├── solid_isp_dip.py
│   └── test_solid_isp_dip.py
│
└── viernes/
    └── uart_driver/
        ├── config.py
        ├── parsers.py
        ├── device.py
        ├── recorder.py
        │
        └── tests/
            ├── test_config.py
            ├── test_parsers.py
            ├── test_device.py
            └── test_recorder.py
---

            Lunes — Python moderno para sensores

El primer día trabajamos con una estructura llamada Reading.

Esta estructura representa una lectura de un sensor de presión.
---

Martes — Máquina de estados

El martes llevamos una idea común de sistemas embebidos al mundo de Python.

Creamos una máquina de estados orientada a objetos.
----

Miércoles — SOLID: SRP, OCP y LSP

El miércoles comenzamos a aplicar los principios SOLID utilizando el dominio de sensores de presión.

Para cada principio mostramos un ejemplo que presenta problemas y otro que busca resolverlos.
----

Jueves — SOLID: ISP y DIP

El jueves completamos los cinco principios SOLID.
---

Viernes — El Driver Modernizado

El viernes juntamos varias de las ideas anteriores en un ejercicio integrador.

Creamos un pequeño driver UART organizado en diferentes componentes.
---

Estado final de la Semana 

Al terminar la semana se cumplen los principales objetivos técnicos:

 Python moderno con type hints.
 Dataclasses.
 Enums.
 Protocols.
 Máquina de estados orientada a objetos.
 SRP.
 OCP.
 LSP.
 ISP.
 DIP.
 Driver UART modernizado.
 Parser Modbus.
 Parser NMEA.
 Persistencia JSON-lines.
 Tests automatizados.
 Cobertura superior al 70%.
 Ruff sin errores.
 Mypy sin errores.