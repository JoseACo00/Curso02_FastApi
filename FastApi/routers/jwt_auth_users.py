from fastapi import APIRouter, Depends, HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCES_TOKEN_DURATION = 2
SECRET = "fd349d955ea45b7e001e94c22898c60e5d67a101d583b09230682cabc0960aaa98b7d80216572c5d"

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

crypt = CryptContext(schemes=["bcrypt"])

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
        "password": "$2a$12$zKCS2deguUrCy0ihKeUiIeAxY1VihDG8W4mkLR8QFuz4gu8Rzzpcq"
    },
    "joselex": {
        "username": "joselex",
        "full_name": "Jose MArtin",
        "email": "Joselepe0@gmail.com",
        "disabled": True,
        "password": "$2a$12$nDB1.pF9/QqQzN75Gzm0WuF5x4ONt0V8Jbi4XIAVtCOIJQcwoVxSG"
    }   
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):
    #ERROR
    exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Credenciales de autenticacion invalidas", 
                headers= {"WWW-Authenticate": "Bearer"})
    
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        
    except JWTError:
        raise exception

    return search_user(username)

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="USUARIO DESAHABILITADO")
    return user

@router.post("/login")
async def entrar(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user_db(form.username)
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail='La contraseña no es correcta')
    
    expire = datetime.utcnow() + timedelta(minutes=ACCES_TOKEN_DURATION)

    acces_token = {"sub": user.username, "exp": expire}

    # CORREGIDO: Usar encode en lugar de decode
    token = jwt.encode(acces_token, SECRET, algorithm=ALGORITHM)

    return {"access_token": token, "token_type": "bearer"}



@router.get("/user/me")
async def userme(user: User = Depends(current_user)):
    return user