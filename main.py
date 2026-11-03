from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)
#PARA RODAR O CÓDIGO RODAR ESTE COMANDO NO TERMINAL:
# uvicorn main:app --reload


#endpoint 
#dominio.com/pedidos/lista
