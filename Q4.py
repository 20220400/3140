from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

def read_encode():
    with open("./Q4files/Encrypted4", "rb") as text_encoded:
        encode = text_encoded.read()

    with open("./Q4files/.key.txt", "rb") as f:
        key = f.read()

    return encode, key

def decrypt():
    encode, key = read_encode()
    iv = encode[:16]  # Assuming the IV is the first 16 bytes of the encoded data
    ciphertext = encode[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    msg_decrypt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    print("Decrypted Message:", msg_decrypt.decode())

    return msg_decrypt

def main():
    decrypted_message = decrypt()
    # You can do further processing with the decrypted message here

if __name__ == "__main__":
    main()
