from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("FERNET_KEY").encode()
f = Fernet(key)

encrypted_input = input(" encrypted password: ").encode()
decrypted = f.decrypt(encrypted_input)

print(decrypted.decode())
