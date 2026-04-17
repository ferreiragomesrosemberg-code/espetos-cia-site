from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.cardapio import Cardapio

router = APIRouter(prefix="/cardapio", tags=["Cardápio"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar_cardapio(db: Session = Depends(get_db)):
    return db.query(Cardapio).all()

@router.post("/")
def criar_item(nome: str, descricao: str, preco: float, db: Session = Depends(get_db)):
    novo_item = Cardapio(nome=nome, descricao=descricao, preco=preco)
    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)
    return novo_item
