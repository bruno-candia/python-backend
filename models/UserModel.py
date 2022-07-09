from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
  id: str = Field(...)
  name: str = Field(...)
  email: EmailStr = Field(...)
  password: str = Field(...)
  photo: str = Field(...)


  class Config:
    schema_extra = {
      "user": {
        "name": "Bruno Costa Candia",
        "email": "exemplo@email.com",
        "password": "SeNha123!",
        "photo": "minhaFoto.png"
      }
    }

class UserCreateModel(BaseModel):
  name: str = Field(...)
  email: EmailStr = Field(...)
  password: str = Field(...)
  photo: str = Field(...)


  class Config:
    schema_extra = {
      "user": {
        "name": "Bruno Costa Candia",
        "email": "exemplo@email.com",
        "password": "SeNha123!",
        "photo": "minhaFoto.png"
      }
    }