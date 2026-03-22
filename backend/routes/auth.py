from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User
from schemas.user import UserCreate, UserLogin
from auth.jwt_handler import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ REGISTER
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    email = user.email.strip().lower()

    # check if user exists
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    # create new user
    new_user = User(
        username=user.username,   # ✅ important
        email=email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }

# ✅ LOGIN
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    email = user.email.strip().lower()

    db_user = db.query(User).filter(User.email == email).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="User not found")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer",
        "username": db_user.email.split("@")[0]   # 🔥 or add real username column later
    }
