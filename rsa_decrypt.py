from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64

def rsa_decrypt(encrypted_data_path, private_key_path):
    with open(private_key_path, "r") as key_file:
        rsa_key = RSA.import_key(key_file.read())

    cipher = PKCS1_OAEP.new(rsa_key)

    with open(encrypted_data_path, "r") as enc_file:
        encrypted_data = base64.b64decode(enc_file.read())

    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode()

# Example usage
decrypted_data = rsa_decrypt("encrypted_data.txt", "patient_private.pem")
print("Decrypted Data:", decrypted_data)
