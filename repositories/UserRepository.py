import motor.motor_asyncio
from bson import ObjectId

from decouple import config
from models.UserModel import UserCreateModel
from services.AuthService import generate_cryptographic_password

MONGODB_URL = config("MONGODB_URL")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = client.devagram

user_collection = database.get_collection('user')

def user_helper(user):
  return {
    "id": str(user["_id"]),
    "name": user['name'],
    "email": user['email'],
    "password": user['password'],
    "photo": user['photo']

  }

async def create_user(user: UserCreateModel) -> dict:
  user.password = generate_cryptographic_password(user.password)
  created_user = await user_collection.insert_one(user.__dict__)
  new_user = await user_collection.find_one({ "_id": created_user.inserted_id })
  return user_helper(new_user)

async def list_users():
  return user_collection.find()

async def search_user_to_email(email: str) -> dict:
  user = await user_collection.find_one({"email": email})

  if user:
    return user_helper(user)

async def update_user(id: str, user_data: dict):
  user = await user_collection.find_one({"_id": ObjectId(id) })

  if user:
    updated_user = await user_collection.update_one(
      {"_id": ObjectId(id)},
      {"$set": user_data}
    )

    return user_helper(updated_user)

async def delete_user(id: str):
  user = await user_collection.find_one({"_id": ObjectId(id) })

  if user:
    await user_collection.delete_one({"_id": ObjectId(id)})