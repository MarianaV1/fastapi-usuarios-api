from fastapi import FastAPI, HTTPException
from db.db import client
from controller.libroCRUD import router as libros_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "https://vega-usuarios-api.azurewebsites.net"
    "http://vega-usuarios-api.azurewebsites.net"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Puedes especificar métodos específicos ['GET', 'POST', etc.]
    allow_headers=["*"],
)

app.include_router(libros_router, tags=["libros"], prefix="/libros")
# MongoDB connection URL
@app.on_event("shutdown")
def shutdown_db_client():
    client.close()