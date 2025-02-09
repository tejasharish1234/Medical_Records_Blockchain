from Crypto.PublicKey import RSA

def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Generate keys for a patient
private_key, public_key = generate_rsa_keys()

# Save keys to files
with open("patient_private.pem", "wb") as priv_file:
    priv_file.write(private_key)

with open("patient_public.pem", "wb") as pub_file:
    pub_file.write(public_key)

print("RSA Keys Generated and Saved.")
