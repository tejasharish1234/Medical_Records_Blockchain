import ipfshttpclient

def download_from_ipfs(cid):
    client = ipfshttpclient.connect()
    return client.cat(cid).decode()

# Example: Retrieve encrypted data from IPFS
cid = "QmccLKrMwzmAKZsLp7NL8iwHhbb4NaGipjdVkmW9AJpuHE"
encrypted_data = download_from_ipfs(cid)

# Save locally
with open("retrieved_encrypted.txt", "w") as file:
    file.write(encrypted_data)

print("Encrypted data retrieved and saved.")
