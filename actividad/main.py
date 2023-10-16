import json
import csv
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/v1/contactos", description="Muestra la lsita de todos losm contactos")
async def leer_contactos():
    try:
        with open ("contactos.csv", mode="r", newline ="") as file:
            csv_reader = csv.DictReader(file)
            contactos = list(csv_reader)
        return JSONResponse(content=contactos)
    except FileNotFoundError:
        raise HTTPException(satuts_code=404, detail =" NO existe el archivo contatos")


@app.post("/v1/contactos", description="Agregar un nuevlo contacto")
async def nuevo_contacto(contacto:  dict):
    try:
        with open("contactos.csv", mode="a", newline="") as file:
            fieldnames =["id_contacto", "nombre", "primer_apellido", "segundo_apellido", "email", "telefono"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(contacto)
            return JSONResponse(content=contacto, status_code=201) 
    except Exception:
        raise HTTPException(status_code=500, detail="NO se agrego el contacto")
    

@app.put("/v1/contactos/{id_contacto}", description="Actualizar un contacto")
async def actualizar_contacto(id_contacto: int, nuevo_contacto: dict):
    try:
        with open("contactos.csv", mode="r+", newline="") as file:
            csv_reader = csv.DictReader(file)
            contactos = list(csv_reader)

            contactos_actualizados = []
            contactos_encontrado = False
            for contacto in contactos:
                if int(contacto["id_contacto"]) == id_contacto:
                    contacto_actualizado = {**contacto, **nuevo_contacto}
                    contactos_actualizados.append(contacto_actualizado)
                    contactos_encontrado = True
                else:
                    contactos_actualizados.append(contacto)
            if not contactos_encontrado:
                raise HTTPException(status_code=404, detail="NO Se encontró el contacto")

            file.seek(0)# *seek*, sirve para mover el puntero del archivo pocision expecifica, en este caso, se utiliza para mover el puntero del archivo. 0 significa al principio y "file" archivo

            fieldnames = ["id_contacto", "nombre", "primer_apellido", "segundo_apellido", "email", "telefono"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contactos_actualizados)

            file.truncate() #  es un metodo que se utiliza para cortar "eliminar" parte de un archivo en este caso, desde la posición actual del puntero hasta el final del archivo.

        return JSONResponse(content=nuevo_contacto)
    except Exception:
        raise HTTPException(status_code=400, detail="NO se pudo actualizar el contacto")

@app.delete("/v1/contactos/{id_contacto}", description="Borra un contacto mediante su ID")
async def borrar_contacto(id_contacto: int):
    try:
        with open("contactos.csv", mode="r", newline="") as file:
            csv_reader = csv.DictReader(file)
            contactos = list(csv_reader)

        contactos_actualizados = []
        contacto_borrado = False
        for contacto in contactos:
            if int(contacto["id_contacto"]) == id_contacto:
                contacto_borrado = True
            else:
                contactos_actualizados.append(contacto)

        if not contacto_borrado:
            raise HTTPException(status_code=404, detail="No se pudo encontrar el contacyo")
        with open("contactos.csv", mode="w", newline="") as file:
            fieldnames = ["id_contacto", "nombre", "primer_apellido", "segundo_apellido", "email", "telefono"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contactos_actualizados)
        return JSONResponse(content={"mensaje": "Se eliminó el contacto"})
    except Exception:
        raise HTTPException(status_code=500, detail="Ocurrio un error y no se pudo eliminar")



@app.get("/v1/contactos", description="Se Buscara contactos por el nombre")
async def buscar_contactos(nombre: str = Query(..., description="NOmbre del contacto a buscar")):
    try:
        with open("contactos.csv", mode="r", newline="") as file:
            csv_reader = csv.DictReader(file)
            contactos = list(csv_reader)
        contactos_encontrados = [contacto for contacto in contactos if nombre.lower() in contacto["nombre"].lower()]
        if not contactos_encontrados:
            raise HTTPException(statud_code= 404, detail="NO se encotro contactos con ese nombre")
        return JSONResponse(content=contactos_encontrados)
    except FileNotFoundError:
        raise HTTPException(statud_code=404, detail="No existe el archivo contatos")

