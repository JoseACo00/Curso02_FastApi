from fastapi import APIRouter, Depends, HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl='login')


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "josele": {
        "username": "josele",
        "full_name": "Jose Coca",
        "email": "Josele21@gmail.com",
        "disabled": False,
        "password": "Josele21"
    },
    "joselex": {
        "username": "joselex",
        "full_name": "Jose MArtin",
        "email": "Joselepe0@gmail.com",
        "disabled": True,
        "password": "Joselepe0"
    }   
}

#FUNCION PARA BUSCAR EL USERDB POR EL USERNAME
def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Credenciales de autenticacion invalidas", 
            headers= {"WWW-Authenticate": "Bearer"})
    return user

#SE PONE LA MISMA URL QUE ARRIBA EL AOTH2
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail='La contraseña no es correcta')
    
    return {"access_token": user.username , "token_type": "bearer"}


@router.get("/user/me")
async def me(user: User = Depends(current_user)):
    return user