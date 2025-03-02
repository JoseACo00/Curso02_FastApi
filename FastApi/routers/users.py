from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel


#HAY ERROR EN ESTE PY ARREGLAR
router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

#INICIAR SERVER uvicorn users:router --reload

#ENTIDAD USER
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    edad: int

# Lista de usuarios usando parámetros nombrados
users_list = [
    User(id=1, name='jose', surname='Coca', url='github.com/josetio.es', edad=24),
    User(id=2, name='iker', surname='Toca', url='github.com/iker.es', edad=24),
    User(id=3, name='ramon', surname='Poca', url='github.com/ramon.es', edad=24),
]

#GET
@router.get("/")
async def users():
    return users_list

#PATH
@router.get("/{id}")
async def get_user(id: int):
    return sear_user(id)

#POR QUERY
# Endpoint para buscar usuario por Query Parameter
# @router.get("/")
# async def user(id: int):
#     return sear_user(id)


#POST

@router.post('/', status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(sear_user(user.id)) == User:
        return {'Error': 'El usuario ya existe con el id: {}'.format(user.id)}
  
    users_list.append(user)
    return user

#PUT
@router.put("/", status_code=status.HTTP_200_OK)
async def updateuser(user: User):
    found = False

    for index,saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found =True
    if not found:
        return {"Error":"No se actualizo el usuario"}
   
    return user

#DELETE
@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def deleteuser(id: int):
    user_id=sear_user(id)

    if user_id is None:
        return {"error": "No se encontró ese USER id: {}".format(id)}
    
    users_list.remove(user_id)
    return {"OK":"EL USUARIO FUE ELIMINADO CON EL ID: {}".format(user_id)}



#Funcio para buscar usuario
def sear_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"error": "No se encontró ese USER id: {}".format(id)}
    
