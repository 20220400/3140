from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import os

def public_key(key):
    public_key = open(key).read()
    key = RSA.importKey(public_key)
    return PKCS1_v1_5.new(key)

def get_files(file_dir):
    return os.listdir(file_dir)

def verify_signature(file_dir, verifyObject):
    for f in file_dir:
        if f.endswith(".sign"):
            file_name = f.rstrip(".sign")

            with open(f'./Q3files/{file_name}', "rb") as file:
                file_content = file.read()
                h = SHA256.new(data=file_content)

            with open(f'./Q3files/{f}', "rb") as sig:
                signature = sig.read()

            if verifyObject.verify(h, signature):
                print(f"{f} and {file_name}")

def main():
    public_key_file = "Q3pk.pem"
    verifyObject = public_key(public_key_file)
    file_dir = "Q3files"
    files = get_files(file_dir)
    verify_signature(files, verifyObject)

if __name__ == "__main__":
    main()
