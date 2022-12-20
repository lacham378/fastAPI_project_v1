from passlib.context import CryptContext


# default cryptor context use is bcrypt for hashing users passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# set users hash values to be used in the password
def hash(password: str):
    return pwd_context.hash(password)

# verify users plain password to hash password in the database
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)