from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64

def rsa_encrypt(data, public_key_path):
    with open(public_key_path, "rb") as key_file:
        rsa_key = RSA.import_key(key_file.read())
    
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_data = cipher.encrypt(data.encode())
    return base64.b64encode(encrypted_data).decode()

# Example usage
data = "Patient's confidential medical record"
encrypted_data = rsa_encrypt(data, "patient_public.pem")

# Save encrypted data to file
with open("encrypted_data.txt", "w") as enc_file:
    enc_file.write(encrypted_data)

print("Data encrypted and saved.")
