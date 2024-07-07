import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Get the hard-coded RSA public key string
def get_private_key_str():
    return """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDFjdname3JKXjZr5T8ZVnuJO3GanXO52sFxabSch32PIqkF31/
EMj/nBRoEJbTFUQ32VfgTX2GJzNGRBThyjymiIZMs4EGWwU534KlsUAnLG0E3auC
Hm5e3qq6v8OiQAVb9ZijVtowo6lonHdjvTISBTsOgt5hb5m5vYKzg0Q3PQIDAQAB
AoGATIcgUu3ZLtmJbq51RPbQCRA2Kew4uc9s5n4EGzbIw4f9XwaYf14VtusT/qIa
gyeUVxwzTflGvG64Dqq1+ieZKW0zdV1SZpurEaOOG6XoL6bf6jPWwLxfmOpbV0ee
68x6DG4O9Z9ncSxoh+0e+dqvhnNU8tuCzQy0AEW6HRq4G5MCQQDQhfym/DsytfVR
KNYzpLPMK6d7BJn7QLmqfT7eLp7aHY86ZNOcgBnfxXWbQFeAX9KEWjNwQcaMI+a2
6UCPUvK/AkEA8oiB72jRKqmTB/46cDFJ85e50zyqBUGwVjFE2tQ6k74TBg9Tp4Zl
W+zmcvHvMeRKnfsd6bXsspLuYWyp+e9hAwJBAKJSKsKyRkLLchOjflrlMzEUKmOQ
yWzUjbMxm+bI089mg0ApjLCe54VR6KLaC0NbVDzDGpegHDarG8X2/NKU93ECQBVt
Vf1uxzv7q0/DeCo9UIlC2Fn/PA4m1Ytn4utqYJp46nlYlU1xpDbQ4TM6iKVhw+3d
J7FkLzs/m+vji8jXCz0CQH1S119DO0f4e3wd38vzi+vQ7P+cGT1iszvHbECYdtmZ
VLq1IudSzOYhlvVfHlo6++N3Uf9wGi5fhPz/JUBsXr4=
-----END RSA PRIVATE KEY-----"""

def shared_key_decrypt(key_data_priv, key_path_encrypted):

    # Get the RSA private key
    private_key = RSA.import_key(key_data_priv)

    # Read the encrypted shared key from the file
    with open(key_path_encrypted, 'rb') as encrypted_key_file:
        encrypted_shared_key = encrypted_key_file.read()

    # Decrypt the shared key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    shared_key = cipher_rsa.decrypt(encrypted_shared_key)

    # Output the shared key to standard output
    return shared_key.hex()

def main():
    # Get the RSA public key
    private_key_str = get_private_key_str()
    encrypted_key_file_path = '/home/cse/Lab3/Q6files/EncryptedSharedKey'
    shared_key = shared_key_decrypt(private_key_str, encrypted_key_file_path)
    print(shared_key)
    
if __name__ == "__main__":
    main()
