#secure password

"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["pbkdf2_sha512"], default = "pbkdf2_sha512", pbkdf2_sha512__default_rounds = 30000,deprecated="auto")

def encrypt_password(password):
    return pwd_context.encrypt(password)

def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

hash = encrypt_password("password")
print(hash)
print(check_encrypted_password("password123", hash))
"""

#New Version
from passlib.hash import pbkdf2_sha512
def hash_password(password):
    return pbkdf2_sha512.hash(password)

def check_password(password, hashed):
    return pbkdf2_sha512.verify(password, hashed)

"""
hash = hash_password("password")
print(hash)
print(check_password("password123", hash))
"""
