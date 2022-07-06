from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Usuario(BaseModel):
    nome: str
    username: Optional[str] = None
    senha: str

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "mensagem": "Ola mundo, esta e minha primeira API"
    }
@app.get("/api/soma")
def soma():
    return{
        "resultado": 2 + 3
    }

@app.post("/api/login")
def login(usuario: Usuario):
    if usuario.nome == 'bruno123' and usuario.senha == 'senha123':    
        reposta = {
            "mensagem": "Login realizado com sucesso"
        }
    else:
        reposta = {
            "mensagem": "senha ou usuario incorreto"
        }

    return reposta