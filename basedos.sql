SHOW DATABASES;

CREATE DATABASE Biblioteca;

USE Biblioteca;

CREATE TABLE Usuario(id int AUTO_INCREMENT PRIMARY KEY,
					nombre VARCHAR(150) NOT NULL,
					contrasenia VARCHAR(12) NOT NULL,
					permisos int(1) NOT NULL,
					CONSTRAINT chk_permisos CHECK (permisos = 1|| permisos= 2));

CREATE TABLE Articulo(id_artic int AUTO_INCREMENT PRIMARY KEY,
						titulo TEXT NOT NULL,
						resumen TEXT NOT NULL,
						fecha VARCHAR(4) NOT NULL,
						palabras_clave VARCHAR(200),
						fuente_original VARCHAR(90),
						autor VARCHAR(100) NOT NULL,
						descriptor_1 VARCHAR(60),
						descriptor_2 VARCHAR(60),
						descriptor_3 VARCHAR(60));
						
CREATE TABLE Consultas(id_consulta int AUTO_INCREMENT PRIMARY KEY NOT NULL,
					id_artic int NOT NULL,
					fecha_consulta DATETIME DEFAULT CURRENT_TIMESTAMP,
					FOREIGN KEY (id_artic) REFERENCES Articulo(id_artic));
					
CREATE INDEX idx_id_artic ON consultas(id_artic);

CREATE INDEX idx_artic_fecha ON consultas(id_artic, fecha_consulta);

/*Consultas periodicas*/
CREATE TABLE consultas_resumen (
    id_artic INT NOT NULL,
    total_consultas INT DEFAULT 0,
    PRIMARY KEY (id_artic),
    FOREIGN KEY (id_artic) REFERENCES articulo(id_artic)
);

INSERT INTO consultas_resumen (id_artic, total_consultas)
SELECT id_artic, COUNT(*)
FROM consultas
GROUP BY id_artic
ON DUPLICATE KEY UPDATE total_consultas = total_consultas + VALUES(total_consultas);

-- Luego, elimina los registros antiguos de la tabla `consultas`:
DELETE FROM consultas WHERE fecha_consulta < NOW() - INTERVAL 7 DAY;

SELECT a.id_artic, a.titulo, r.total_consultas
FROM articulo a
JOIN consultas_resumen r ON a.id_artic = r.id_artic
ORDER BY r.total_consultas DESC
LIMIT 10;
						
SET GLOBAL local_infile=1;

LOAD DATA  LOCAL INFILE 'C:/Users/agaud/Downloads/xd.txt'  INTO TABLE Articulo
CHARACTER SET latin1
FIELDS TERMINATED BY '\t' 
LINES TERMINATED BY '\n' ;

INSERT INTO Usuario(id, nombre, contrasenia, permisos) VALUES (DEFAULT, "noemi", "1234", 1);
INSERT INTO Usuario(id, nombre, contrasenia, permisos) VALUES (DEFAULT, "noemiuser", "1234", 2);

SELECT id, nombre, contrasenia, permisos FROM Usuario WHERE (nombre = "noemi" AND contrasenia = "1234")