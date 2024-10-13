from fastapi import FastAPI, Depends, Form, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database import DATABASE_URL, SessionLocal
from app.models import Merchant, Product, User
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware






app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserRegister(BaseModel):
    email: EmailStr
    username: str
    password: str


# Modèle pour la création d'un produit
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    username: str

# Modèle pour la réponse des produits
class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    username: str

    class Config:
        orm_mode = True




class UserProfile(BaseModel):
    username: str
    email: str






@app.post("/api/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = pwd_context.hash(user.password)
    new_user = User(username=user.username, email=user.email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()

    return {"message": "Registration successful"}


# Configurer le middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou liste des origines spécifiques autorisées
    allow_credentials=True,
    allow_methods=["*"],  # Ou liste des méthodes spécifiques autorisées
    allow_headers=["*"],  # Ou liste des en-têtes spécifiques autorisés
)


def pwd_context_verify(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)



@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not pwd_context_verify(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Nom d'utilisateur ou Mot de passe invalide")
    return {"message": "Connexion reussie", "username": db_user.username}

