from cryptography.fernet import Fernet
from subprocess import *

initialChoice = None
key = None
keyStr = None
keyLocation = None
fileLocation = None
fileOutput = None

keyData = None

inputData = None
output = None


def initial_request():
    print("What would you like to do? \n1. Generate a key\n2. Encrypt a file\n3. Decrypt a file\n")
    initialChoice = input()
    if initialChoice == "1":
        key_generation()
    elif initialChoice == "2":
        encryption()
    elif initialChoice == "3":
        decryption()
    else:
        print("Not a valid option")
        call("clear")
        main()
    return


def key_generation():
    key = Fernet.generate_key()
    keyStr = str(key.decode())
    f = open("key.txt", "w+")
    f.write(keyStr)
    f.close()
    print("The key has been written to a file called 'key.txt'.\n")
    return


def encryption():
    print("Path to the encryption key:")
    keyLocation = input()

    print("Path of the file to be encrypted:")
    fileLocation = input()

    print("Path for the file output:")
    fileOutput = input()

    """ Turn key into byte form """
    f = open(keyLocation, "r")
    key = f.readline()
    f.close()
    keyData = key.encode()

    """Creating encryption method"""
    cipher_suite = Fernet(keyData)

    """Getting input data"""
    f = open(fileLocation, "r")
    inputData = f.read()
    f.close()
    info = inputData.encode()

    """Encrypting Data"""
    output = cipher_suite.encrypt(info)

    """Data Storage"""
    f = open(fileOutput + "/" + "Encryption_Output.txt", 'w')
    f.write(output.decode())
    f.close()
    return


def decryption():
    print("Path to the encryption key:")
    keyLocation = input()

    print("Path of the file to be decrypted:")
    fileLocation = input()

    print("Path for the file output:")
    fileOutput = input()

    """ Turn key into byte form """
    f = open(keyLocation, "r")
    key = f.readline()
    f.close()
    keyData = key.encode()

    """Creating encryption method"""
    cipher_suite = Fernet(keyData)

    """Getting input data"""
    f = open(fileLocation, "r")
    inputData = f.read()
    f.close()
    info = inputData.encode()

    """Decrypting Data"""
    output = cipher_suite.decrypt(info)

    """Data Storage"""
    f = open(fileOutput + "/" + "Decryption_Output.txt", 'w')
    f.write(output.decode())
    f.close()
    return


def main():
    initial_request()
    return


main()
