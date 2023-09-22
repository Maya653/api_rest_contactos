# Desing Document: API REST CONTACTOS

## 1. DESCRIPCIÓN
Eemplo de una API RESt para gestionar contactos en una DB utilizando FastAPI

## 2. Objetivo
Realizar un ejemplo de diseño de una API REST de tipo CRUD y su posterior codificación utilizando el framework [FastAPI](https://fastapi.tiangolo.com/).

## 3. Diseño de la BD
Para este ejemplo se utilizará el gestor de bases de datos [SQLite3](https://www.sqlite.org/) con las siguientes tablas:


|NO.|Campo|Tipo|Restricciones|
|--|--|--|--|--|
|1|id_contactos|int|PRIMARY KEY|Llave primaria de la tabla|

## 3.2 SCRIPT

```sql
X-CREATE TABLE...
```
CREATE TABLE contactos (
    id_contacto INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    primer_apellido VARCHAR(30),
    segundo_apellido VARCHAR(30),
    email VARCHAR(50),
    telefono VARCHAR(13),
    PRIMARY KEY (id_contacto)
);
