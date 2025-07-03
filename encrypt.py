from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("FERNET_KEY").encode()
f = Fernet(key)

password = input("Enter password  ").encode()
encrypted = f.encrypt(password)

print(encrypted.decode())
