import ipfshttpclient

def upload_to_ipfs(file_path):
    client = ipfshttpclient.connect()
    with open(file_path, "r") as file:
        content = file.read()
    res = client.add_str(content)
    return res  # Returns CID

# Upload encrypted file
cid = upload_to_ipfs("encrypted_data.txt")
print("File uploaded to IPFS with CID:", cid)
