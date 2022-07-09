from models.UserModel import UserCreateModel
from repositories.UserRepository import (
  create_user,
  search_user_to_email,
  list_users,
  update_user,
  delete_user,
)

async def user_register(user: UserCreateModel):
  try:
    finded_user = await search_user_to_email(user.email)

    if finded_user:
      return {
        "menssage": f'E-mail {user.email} ja cadastrado',
        "data": "",
        "status": 400
      }
    else: 
      new_user = await create_user(user)

      return{
        "message": "Usuario cadastrado com sucesso!",
        "data": new_user,
        "status": 201
      }

  except Exception as error:
    return{
      "message": "Intern Service Error",
      "data": str(error),
      "status": 500
    }