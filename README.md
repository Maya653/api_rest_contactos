# Desing Document: API REST CONTACTOS

## 1. DESCRIPCIÓN
Eemplo de una API RESt para gestionar contactos en una DB utilizando FastAPI

## 2. Objetivo
Realizar un ejemplo de diseño de una API REST de tipo CRUD y su posterior codificación utilizando el framework [FastAPI](https://fastapi.tiangolo.com/).

## 3. Diseño de la BD
Para este ejemplo se utilizará el gestor de bases de datos [SQLite3](https://www.sqlite.org/) con las siguientes tablas:


|NO.|Campo|Tipo|Restricciones|
|--|--|--|--|
|1|id_contactos|int|PRIMARY KEY|Llave primaria de la tabla|

## 3.2 SCRIPT

```sql
X-CREATE TABLE...
```
CREATE TABLE contactos (
    id_contacto INT AUTO_INCREMENT NOT NULL,
    nombre             VARCHAR(50) NOT NULL,
    primer_apellido    VARCHAR(30) NOT NULL,
    segundo_apellido   VARCHAR(30) NOT NULL,
    email              VARCHAR(50) NOT NULL,
    telefono           VARCHAR(13) NOT NULL,
    PRIMARY KEY (id_contacto)
);

TABLA DE CONTACTOS
|Campo|Tipo|Restriciones|
|--|--|--|
| id_contacto|INT AUTO_INCREMENT|NOT NULL|
|nombre|VARCHAR(50)|NOT NULL|
|primer_apellido|VARCHAR(30)|NOT NULL|
|segundo_apellido|VARCHAR(30)|NOT NULL|
|email|VARCHAR(50)|NOT NULL|
|telefono|VARCHAR(13)|NOT NULL|
|--|--|PRIMARY KEY (id_contacto)

ENDPOINT
GET
|NO.|Propiedad|Descripción|
|--|--|--|
|1|Description|Obtener una lista de contactos en la API|
|2|Sumarry|Obtener una lista de contactos|
|3|Method|GET|
|4|Enpoint|http://localhost:8000/contactos|
|5|Query Param|Parametros de consulta "nombre"|
|6|Path Param| NA|
|7|Data||
|8|Version| v1|
|9|Status Code(conexión)
|10|Responce type| 200|
|11|Responce||
|12|Curl| curl -x 'GET' htpp://localhost:8000/contactos -H accept application/json
|13|Status Code(error)| { error: "El recurso solicitado no existe" }|
|14|Responce type(error)|aplication/json
|15|Responce (error)||

POST
|NO.|Propiedad|Descripción|
|--|--|--|
|1|Description|Endpoint para crear un nuevo contacto en la API|
|2|Sumarry|Endpoint para crear un nuevo contacto|
|3|Method|POST|
|4|Enpoint|http://localhost:8000/contactos|
|5|Query Param|NA|
|6|Path Param| NA|
|7|Data||
|8|Version| v1|
|9|Status Code(exito)|201 Creado|
|10|Responce type| application/json|
|11|Responce||
|12|Curl| curl -x 'Post' htpp://localhost:8000/contactos -H accept application/json
|13|Status Code(error)| 400|
|14|Responce type(error)|aplication/json
|15|Responce (error)|{ error: "Los datos son incorrectos"}|

PUT 
|NO.|Propiedad|Descripción|
|--|--|--|
|1|Description|Actualizar un contacto en la API|
|2|Sumarry|Actuailizar un contacto|
|3|Method|PUT|
|4|Enpoint|http://localhost:8000/contactos|
|5|Query Param|NA|
|6|Path Param| NA|
|7|Data||
|8|Version| v1|
|9|Status Code(exito)|201 Creado|
|10|Responce type| application/json|
|11|Responce||
|12|Curl| curl -x 'Post' htpp://localhost:8000/contactos -H accept application/json
|13|Status Code(error)| 400|
|14|Responce type(error)|aplication/json
|15|Responce (error)|{ error: "Los datos son incorrectos"}|

DELETE 
|NO.|Propiedad|Descripción|
|--|--|--|
|1|Description|Eliminar un  contacto en la API|
|2|Sumarry|Eliminar un contacto|
|3|Method|DELETE|
|4|Enpoint|http://localhost:8000/contactos/{id}|
|5|Query Param|id (es un paramatro de ruta que representa un identificador del contacto que se pueda elimikar)|
|6|Path Param| NA|
|7|Data||
|8|Version| v1|
|9|Status Code(exito)|204 Creado|
|10|Responce type| application/json|
|11|Responce||
|12|Curl| curl -x 'Delete' htpp://localhost:8000/contactos -H accept application/json
|13|Status Code(error)| 400|
|14|Responce type(error)|aplication/json
|15|Responce (error)|{ error: "Los datos son incorrectos"}|
