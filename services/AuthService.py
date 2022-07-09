from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_cryptographic_password(password):
  return pwd_context.hash(password)


def verify_password(password, cryptographic_password):
  return pwd_context.verify(password, cryptographic_password)
