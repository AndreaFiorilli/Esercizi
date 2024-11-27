# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# # Per iniziare generiamo una coppia di chiavi e le stampiamo
# # Generating RSA Key Pair
# # Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA4XgKRs1ykDlHxnG1AMePNELGJxM5gw0ktr97SzdgkUdhminK\nWOXrOmFGXXA+3NYNM0eqV0IbwK+Klcao/Ec1d/eC3Aj0oMPx3SSNIQQCc2Ap11vC\nPM7EHhS9xiEOJkL+FqQotzm6SlVy+RqyuYtY4jEM0A1rjIHvUXycGzz1DEcfAsFY\niqdI17S7sHDe/6QP0W+e9a3jYiDxb8q792bDSflZXsDo+Y5RzBZWm3UZ4mWzG4b1\netbyctb+CUNbOd0lC0ODeREdh/bh7ZwpAGaPAFdWUPLnUmSWOg6tqYadSCOZho93\n8zpXn7Nax+FUTJGNWEQqq7qjcf8pEbr/9JnqSwIDAQABAoIBAAkc5HFwe/5nSkbe\nMVN66AdT4ZVnugMuz0/m6lv5Ei6dBM1fKLNcy5vxnY9I6kmGX0SLfiTbt6pwjeM4\nLdFQgXvmpZkwxXkP97Zunpj52Vgsx/7RJxx1EPPUS8f2bbokgAeN6AAL1cM2XpjB\n4v0L1vJWytlH3ukawVT4+ohBTPg2KOgdiROue0YwLVPGeB+Nz+2uulVUa7hBPuRx\nH5zrGVHaHbAjQcDWt4/DT+ccB5N6M+piGnv+hSYw+LoogkeQc53r8NPfyy382LC7\n+0jkWY+BryHGFhe4OsJK4aSXu8eZIpzd2o7zkvu0vkYCsAICDZyt+UM/+HP0v+Vw\nZEomdgkCgYEA5gl0M2icAPNBgPhlvckiUfFl5KeeQYQBv/GQ3/bEx8SaVmNAGHdJ\nQUqD0637r43XJwzZxoBsrlaI8ozgzxmMquVHYKEODztee0F0Itjt/ngStOZYJRkR\nxXseA1pyAGeCq5W7ojro7z+Na+OJdz/VAHXyuswkAHRX6vj8zPREZKMCgYEA+uqZ\nwDq3J4w7m6Com855KHG/2zD6aeR4vO+ClJfIgVlCIGs/bXxH1Bqn+62+GMrXUObG\nnUIgUVjHFg5czYx4slxHSWhPLP1LY5JuirNivkKHvO63Dodh8VBEOOWefbmsGpt1\ntWT+/aalWONx6GtET4oanKW5Goynd1uDi4Z4ljkCgYEAvYnGm+EywTmtnEWPFxwV\n0iyzxv4xUEwjYPL6av8Zznv4qvtmQYJv8oMiMZUmTtTxFPTqrzr70X3touRfC2VC\n2UDHWh/5xKUnSSl6NohFOKnYyAMPV6nbUbsK1Lp+OkUPjq92BcrCSPc1YFL/3ijT\nKWkF0dIIS/OQyUPUkE8n1z8CgYBNPhFM0wZ1Hz9uXlvpcvtrTvEf+gjstk/Q4e6R\n7dPkteScdEeXXc4C5p3V5ZuCqFb2acS0vpmSUUEgchVxlY/GYI/1ci4FjIg7w+VR\nv31jUrnUmKwzxcuJ7QrDdTSAQbtQiZEH4Wp6DWYTYhk70mG6FqqwlHfSS4B2Ru7M\n8f2HSQKBgEaWwtngjOAwmwNSDP4KDKSFYBNVThpyEBxG+O4xNxmrNyL7JPU2TJDd\nEw5cNfP2RASaoXWNsZLB/FLyWC8QHb9xdFKf9tJ4RGHzTSweBdjDWiBAwIygwhU4\nuuN2XTsSrSVbRLDbM1Fh0VQmTam9G5ob63y8uhdh7zlruIVBclb/\n-----END RSA PRIVATE KEY-----"
sPub = "aipcOuwuGpYhNWFRyYw2yU+vOqJ1zSIsvO+ap57fpTa608P3SRx8X+csO8tCVbFpMsHf9zGskjWb3pnwqq75gdCUUTEryAtxsKRsFnFwQ/KdfsTtzUfiwY+ubsyAFTims9Am5HIDug65rxHpunH6D1mNne+oabTQnsjg7UA1fc0HmBDk2roR9cjVFcZiTJGF4BuEB7G1ORCeSjPAvTo7cukRMxU55uUyeAykoQlg8aVnN8FK6Vp9PjPlOtqr+4tsO1KpECpEpYCPbgpmJr3VRemXfuLA+YeMRYYVA+NCQBIWdZVf6W9pdx7ikVfbgdULjCZHQbbN501i3WxHfHefMA=="

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
#message = "ciao"
#encrypted_message = encrypt_message(message, public_key)
decrypted_message = decrypt_message("aipcOuwuGpYhNWFRyYw2yU+vOqJ1zSIsvO+ap57fpTa608P3SRx8X+csO8tCVbFpMsHf9zGskjWb3pnwqq75gdCUUTEryAtxsKRsFnFwQ/KdfsTtzUfiwY+ubsyAFTims9Am5HIDug65rxHpunH6D1mNne+oabTQnsjg7UA1fc0HmBDk2roR9cjVFcZiTJGF4BuEB7G1ORCeSjPAvTo7cukRMxU55uUyeAykoQlg8aVnN8FK6Vp9PjPlOtqr+4tsO1KpECpEpYCPbgpmJr3VRemXfuLA+YeMRYYVA+NCQBIWdZVf6W9pdx7ikVfbgdULjCZHQbbN501i3WxHfHefMA==", key_pair)

#print("Original Message:", message)
#print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
