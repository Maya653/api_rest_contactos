from fastapi import FastAPI
from fastapi import status

app= FastAPI()

@app.get("/",
         status_code=status.HTTP_200_OK,
         summary="Enpoint raíz"
)
async def root():
    return {"Hello": "World"}