from fastapi import APIRouter, Body, HTTPException
from models.UserModel import UserCreateModel
from services.UserService import (
  user_register
)

router = APIRouter()

@router.post("/", response_description="Rota para criar um novo usuario")
async def rota_criar_usuario(user: UserCreateModel = Body(...)):
  try:
      
    result = await user_register(user)

    if not result['status'] == 201:
      raise HTTPException(status_code = result['status'], detail = result['menssage'])

    return result
  except Exception as erro:
    print(erro)

    return {
      "mensage": "Internal Sistem Error"
    }
    