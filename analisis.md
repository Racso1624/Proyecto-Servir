# Resolución del Escenario de Análisis

### Introducción a la resolución
Se plantea un problema en el cuál se debe buscar la solución utilizando herramientas del sistema previamente creado y buscar la forma de crear nuevas herramientas que apoyen la solución. En este caso se debe de solucionar una problemática en la cuál los empleados de la empresa deben de tener una asistencia que se puede marcar durante cada uno de los días de su trabajo en distintos centros de trabajo de la empresa, por lo tanto se debe de buscar una forma en la que se puede optimizar y lograr brindar una solución para que las personas que manejan la información de los empleados logren ingresar los datos necesarios al sistema.

### Objetivos

- Obtener la asistencia de los empleados.
- Mediante la asistencia lograr el control con los centros de trabajo.
- Controlar la planificación mediante la asistencia

### Suposiciones

Para la resolución de este problema se tienen las siguientes suposiciones:
- Los centros de trabajo principalmente solo sirven como distribución para los empleados con los mismos departamentos creados, los empleados pueden estar en el mismo departamento solamente que pueden cambiar de centro de trabajo en cualquier momento.
- Los empleados siguen utilizando el mismo sistema de códigos creados y no es necesario brindar una conexión directa con el centro de trabajo debido a la facilidad que se tiene de cambiar de centro.
- Los centros de trabajo serán tomados como una nueva entidad.

### Resolución

#### Tablas de Almacenamiento

Para abordar la parte de almacenamiento en el sistema de datos se proponen crear dos nuevas tablas para guardar información:

Centro de Trabajo
- Código del Centro
- Nombre del Centro
- Ubicación
- Descripción de Operaciones
- Supervisor del Centro
- Número de Telefono

Asistencia
- Código de Asistencia (Campo Correlativo Automático)
- Código de Empleado
- Código de Centro
- Fecha
- Hora de Llegada
- Hora de Salida

#### Pantallas

Creación de Centros:

Pantalla en la cuál se crearan los centros de trabajos en los que los trabajadores pueden realizar las operaciones diarias. Esto incluye la inclusión de las pantallas en las cuáles se pueden listar los centros, eliminar y realizar la actualización de la información de cada uno de estos.

Asistencia:

Pantalla en la que se realizará el llenado de la asistencia diaria de cada uno de los empleados de la empresa, en este se ingresará la información necesaria para conocer las horas en las que el empleado trabajó y la fecha se automatizará.

Revisión de Asistencia:

Pantalla en la que se realizará el listado de la asistencia marcada de cada uno de los empleados, utilizando el código personal de empleado para vincular y mostrar la información personal de asistencia.

#### Procesos

Para la efectividad de la solución se pueden crear procesos en los cuáles los empleados o supervisores marcarán la asistencia diaria de cada uno de estos mediante el código del centro y del empleado, además de lograr brindar la información para conocer las horas trabajadas del empleado.

Para brindar más información se puede realizar más pantallas que puedan brindar estadísticas de los empleados dependiendo de la necesidad que se tenga y la forma en la que la información sea necesaria para brindar resultados en las planificaciones mensuales.

#### Consultas

Para una mejor resolución del problema se realizarán las siguientes consultas a las personas encargadas de llevar el proceso de la implementación de la asistencia y planificaciones mensuales:
- ¿Cuáles son los datos principales que deben de obtener en la el manejo de la asistencia con los empleados?
- ¿Qué estadísticas importantes pueden brindar datos certeros para la planificación mensual de los empleados?
- ¿Es importante que se tenga una conexión directa entre el centro y el empleado?