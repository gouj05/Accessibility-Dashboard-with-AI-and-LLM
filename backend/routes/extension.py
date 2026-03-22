from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.extension import Extension

router = APIRouter()

@router.get("/extensions/{name}")
def get_extension(name: str, db: Session = Depends(get_db)):
    ext = db.query(Extension).filter(Extension.name == name).first()

    if not ext:
        return {"error": "Extension not found"}

    return {
        "name": ext.name,
        "description": ext.description,
        "image": ext.image,
        "download": ext.download
    }