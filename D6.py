import os
import sys
import subprocess
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Util.Padding import pad, unpad
import ast

#AES.BLOCK_SIZE = 16

def file_path():
    return '/home/cse/Lab3/Q6files/victims' 

def decrypt_files(file_path, input_key):
    key = input_key
    for victim in os.scandir(file_path):
        if victim.path.endswith('.encrypted'):
            f = open(victim.path, 'rb')
            iv = f.read(16)
            data = f.read()
            cipher_aes = AES.new(key, AES.MODE_CBC, iv = iv)
            decrypted_data = unpad(cipher_aes.decrypt(data), AES.block_size)
            deMess = decrypted_data.decode("utf-8")
            with open(victim.path.strip('.encrypted')+'t', 'wb') as f:
                f.write(decrypted_data)
            os.remove(victim.path)      
    return decrypted_data     

def main():
    # pass it as a parament
    key = b'56a9a2f857a8ebd86fd4504374dfe2d7'
    #key = ast.literal_eval(key)
    

    path_file = file_path()
    files_decrypt = decrypt_files(path_file, key)
    print(files_decrypt)
    
if __name__ == "__main__":
    main()



