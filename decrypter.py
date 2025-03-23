import os
import pyaes

def decrypt_file(encrypted_file_name, key, original_file_name):
    try:
        
        with open(encrypted_file_name, "rb") as file:
            file_data = file.read()

        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        with open(original_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        os.remove(encrypted_file_name)
        print(f"Arquivo '{encrypted_file_name}' descriptografado com sucesso e salvo como '{original_file_name}'.")

    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")

key = b"testeransomwares"

encrypted_file_name = "teste.txt.ransomwaretroll"

original_file_name = "teste.txt"

decrypt_file(encrypted_file_name, key, original_file_name)
