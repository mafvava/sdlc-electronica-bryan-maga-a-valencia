# AI_LOG.md

## Entrada 1 — Definición del proyecto y enfoque del dominio

### Prompt
> Necesito desarrollar un proyecto para la semana 1 de un curso de desarrollo de software orientado a electrónica. El entregable debe incluir una máquina de estados, ejemplos de principios SOLID y un ejercicio integrador de un driver UART. Quiero trabajar con un dominio relacionado con sensores industriales, preferentemente usando lecturas de presión. Ayúdame a definir una idea general que permita que todos los ejercicios tengan relación entre sí y no parezcan proyectos separados.

### Qué produjo la IA
La IA propuso usar como dominio principal un sistema de sensores industriales enfocado en la lectura de presión. A partir de esta idea se planteó que los primeros ejercicios trabajaran con objetos como sensores y lecturas, y que posteriormente los ejemplos de SOLID y el driver UART utilizaran el mismo contexto.

También se propuso manejar diferentes estados de los sensores, tipos de sensores y lecturas con información como valor, unidad, fecha y estado.

### Mi decisión
Decidí utilizar el dominio de sensores industriales y específicamente trabajar con sensores de presión como ejemplo principal.

### Por qué tomé esta decisión
Elegí este enfoque porque permite conectar todos los ejercicios de la semana. La lectura de presión sirve como base para trabajar con objetos y validaciones, la máquina de estados puede representar estados de un sistema, los principios SOLID pueden aplicarse a sensores y almacenamiento, y el driver UART puede simular la comunicación con dispositivos industriales.

La idea fue no agregar funcionalidades solamente por agregar, sino mantener un mismo contexto durante toda la semana.

---

## Entrada 2 — Definición de la estructura de carpetas

### Prompt
> Quiero organizar el proyecto de la semana 1. Me gustaría que dentro de `semana1` existan carpetas separadas por día, por ejemplo `lunes`, `martes`, `miercoles`, `jueves` y `viernes`. Dentro de cada carpeta quiero colocar los archivos de código y sus respectivos tests. El viernes tendrá además un ejercicio integrador llamado `uart_driver`. Ayúdame a proponer una estructura que mantenga todo organizado y que permita ejecutar los tests fácilmente.

### Qué produjo la IA
La IA propuso una estructura organizada por días:

- `semana1/lunes` para el trabajo relacionado con lecturas de sensores.
- `semana1/martes` para la máquina de estados.
- `semana1/miercoles` para SRP, OCP y LSP.
- `semana1/jueves` para ISP y DIP.
- `semana1/viernes/uart_driver` para el ejercicio integrador.

También se propuso colocar los archivos de prueba junto con cada ejercicio y, dentro del driver UART, tener una carpeta específica para `tests`.

### Mi decisión
Decidí mantener la estructura organizada por días porque coincide con la forma en la que se fue desarrollando el trabajo durante la semana.

La estructura final quedó aproximadamente así:

```text
semana1/
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
        ├── device.py
        ├── parsers.py
        ├── recorder.py
        └── tests/
            ├── test_config.py
            ├── test_device.py
            ├── test_parsers.py
            └── test_recorder.py