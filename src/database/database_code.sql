/*
Creado por Oscar Fernando López Barrios
Proyecto Servir
Prueba Técnica
*/

-- Codigo para crear la entidad departamento
create table departamento(
	id varchar(20) primary key,
	nombre varchar(50),
	descripcion varchar(70)
)

-- Codigo para crear la entidad empleado
create table empleado(
	codigo serial primary key,
	id varchar(10),
	nombres varchar(50),
	apellidos varchar(50),
	fecha_nacimiento date,
	id_departamento varchar(20),
	FOREIGN KEY (id_departamento) REFERENCES departamento(id)
)

-- Funcion para actualizar el codigo del empleado con el 
-- formato de EMP-XXXX
CREATE OR REPLACE FUNCTION ActualizarCodigoEmpleado()
RETURNS TRIGGER AS $$
BEGIN
    NEW.id = 'EMP-' || LPAD(NEW.codigo::TEXT, 4, '0');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger que se activa antes de insertar un dato de empleado
CREATE TRIGGER TriggerActualizarCodigo
BEFORE INSERT ON empleado
FOR EACH ROW
EXECUTE FUNCTION ActualizarCodigoEmpleado();