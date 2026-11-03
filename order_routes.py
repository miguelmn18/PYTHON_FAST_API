from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("")
async def pedidos():
    return {"mensagem" : "você está acessando a rota de pedido"}
    