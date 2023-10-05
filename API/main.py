import csv
import json
from fastapi import FastAPI
from fastapi import status
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get("/",
         status_code=status.HTTP_200_OK,
         summary="Enpoint raíz")
async def root():
    return {"Hello": "World"}


@app.get("/v1/contactos")   
async def contactos():
    with open("contactos.csv", mode="r", newline="") as file:
        csv_reader = csv.DictReader(file)
        contactos = list(csv_reader)
        contactos_json = json.dumps(contactos)
        response = JSONResponse(content=contactos_json)
    return response
