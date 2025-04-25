from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], default = "pbkdf2_sha256", pbkdf2_sha256__default_rounds = 30000,deprecated="auto")

def encrypt_password(password):
    return pwd_context.encrypt(password)


# secure password
from passlib.context import CryptContext

#Create an object of the class CryptContext
pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                          default="pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds=30000
                          )

#this function receives the unsafe password
# and returns the hashed password

def check_password(hashed_password, user_password):
    return pwd_config.verify(user_password, hashed_password)

# hash = encrypt_password("password123")
# print(hash)