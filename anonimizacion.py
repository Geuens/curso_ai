import os
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from dotenv import load_dotenv

class Anonimizador:

    def __init__(self):
        load_dotenv()

        salt_value = os.environ.get("SALT")
        if salt_value is None:
            raise ValueError("SALT environment variable is not set")

        self.salt = salt_value.encode()
        self.symmetric_key = self.generar_clave_simetrica()
        self.public_key, self.private_key = self.generar_par_claves_asimetricas()

    def hash_con_salt(self, nombre, apellido):
        nombre_completo = nombre + " " + apellido
        nombre_completo_codificado = nombre_completo.encode()
        entrada_con_salt = nombre_completo_codificado + self.salt
        hash_objeto = hashlib.sha256(entrada_con_salt)
        hash_hex = hash_objeto.hexdigest()
        return hash_hex

    def generar_clave_simetrica(self):
        return Fernet.generate_key()

    def cifrar_simetrico(self, nombre):
        f = Fernet(self.symmetric_key)
        nombre_codificado = nombre.encode()
        nombre_cifrado = f.encrypt(nombre_codificado)
        return nombre_cifrado

    def descifrar_simetrico(self, nombre_cifrado):
        f = Fernet(self.symmetric_key)
        nombre_descifrado = f.decrypt(nombre_cifrado)
        return nombre_descifrado.decode()

    def generar_par_claves_asimetricas(self):
        clave_privada = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        clave_publica = clave_privada.public_key()
        return clave_publica, clave_privada

    def cifrar_asimetrico(self, nombre):
        nombre_codificado = nombre.encode()
        nombre_cifrado = self.public_key.encrypt(
            nombre_codificado,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return nombre_cifrado

    def descifrar_asimetrico(self, nombre_cifrado):
        nombre_descifrado = self.private_key.decrypt(
            nombre_cifrado,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return nombre_descifrado.decode()

# Ejemplo de uso
anonimizador = Anonimizador()

nombre_anonimizado_hash = anonimizador.hash_con_salt("Juan", "Pérez")
print("Nombre Anonimizado con Hash:", nombre_anonimizado_hash)

nombre_cifrado_simetrico = anonimizador.cifrar_simetrico("Carlos Garcia")
print("Nombre Cifrado Simétrico:", nombre_cifrado_simetrico)

nombre_descifrado_simetrico = anonimizador.descifrar_simetrico(nombre_cifrado_simetrico)
print("Nombre Descifrado Simétrico:", nombre_descifrado_simetrico)

nombre_cifrado_asimetrico = anonimizador.cifrar_asimetrico("Carlos Garcia")
print("Nombre Cifrado Asimétrico:", nombre_cifrado_asimetrico)

nombre_descifrado_asimetrico = anonimizador.descifrar_asimetrico(nombre_cifrado_asimetrico)
print("Nombre Descifrado Asimétrico:", nombre_descifrado_asimetrico)
