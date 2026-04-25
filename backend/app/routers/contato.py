from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.contato import Contato

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar_contatos(db: Session = Depends(get_db)):
    return db.query(Contato).all()

@router.post("/")
def criar_contato(nome: str, mensagem: str, db: Session = Depends(get_db)):
    novo_contato = Contato(nome=nome, mensagem=mensagem)
    db.add(novo_contato)
    db.commit()
    db.refresh(novo_contato)
    return novo_contato
