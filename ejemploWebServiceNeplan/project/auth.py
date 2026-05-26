import hashlib  # libreria para encriptar.

from config import USERNAME, PASSWORD

def get_credentials():

    hashed_password = hashlib.sha1(           # Crear un objeto hash SHA-1
        PASSWORD.encode("utf-8")              # Convertir la contraseña a bytes para el hashing
    ).hexdigest()                             # Obtener el hash en formato hexadecimal

    return USERNAME, hashed_password