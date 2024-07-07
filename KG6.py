from Crypto.PublicKey import RSA
from Crypto import Random

def generate_keypair():
    # Generate a new RSA key pair
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)

    # Export the private key
    private_key = key.exportKey()
    with open("d.key", "wb") as f:
        f.write(private_key)

    # Export the public key
    public_key = key.publickey().exportKey()
    with open("e.key", "wb") as f:
        f.write(public_key)

if __name__ == "__main__":
    generate_keypair()
