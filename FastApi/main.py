from fastapi import FastAPI
from routers import products,users, basic_auth_users, jwt_auth_users, users_db #SE IMPORTA LO QUE TENEMOS EN ROUTERS 
from fastapi.staticfiles import StaticFiles
app = FastAPI()

#ROUTERS
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

#RECURSO ESTATICO
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get("/main")
async def root():
    return {"Message": "Hola soy el main de fastAPi"}