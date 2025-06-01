CREATE TABLE estudiantes (
    id int PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(50) NOT NULL,
    edad int NOT NULL,
    ciudad varchar(50) NOT NULL,
);

-- Insertar datos de ejemplo en la tabla estudiantes

INSERT INTO estudiantes (nombre, edad, ciudad) VALUES
('Juan Pérez', 20, 'Madrid'),
('Ana García', 22, 'Barcelona'),
('Luis Fernández', 19, 'Valencia'),
('María López', 21, 'Sevilla'),
('Carlos Sánchez', 23, 'Bilbao');

-- Consultando todos los estudiantes
SELECT * FROM estudiantes;
-- Filtrando estudiantes por ciudad
SELECT * FROM estudiantes WHERE ciudad = 'Madrid';
-- Consultando estudiantes mayores de 20 años
SELECT * FROM estudiantes WHERE edad > 20;
