from fastapi import APIRouter #FastAPI NO SE PONE FAST API SOLO EN EL MAIN Y SE IMPORTA EL APIROUTER Y SE PONE EN LA INSTANCIA ROUTER EN VEZ DE APP Y @ROUTER.GET,POST

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

products_list = ["PRODUCTOS1", "PRODUCTOS2", "PRODUCTOS3", "PRODUCTOS4"]

@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id]