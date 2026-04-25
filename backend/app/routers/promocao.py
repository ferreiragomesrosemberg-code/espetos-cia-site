from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.promocao import Promocao

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar_promocoes(db: Session = Depends(get_db)):
    return db.query(Promocao).all()

@router.post("/")
def criar_promocao(titulo: str, desconto: float, db: Session = Depends(get_db)):
    nova_promocao = Promocao(titulo=titulo, desconto=desconto)
    db.add(nova_promocao)
    db.commit()
    db.refresh(nova_promocao)
    return nova_promocao
