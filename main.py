from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)


class main:
    def __init__(self):
        password = input("Ecrivez le mot de passe que vous voulez chiffrer :")
        ciphertext = cipher.encrypt(password)
    def chiffrage(self):
        print("Mot de passe chiffré !")
        voir = input("Voulez vous le voir en étant chiffer, si oui, tapez y, si non, tapez n :")
        if voir == "y":
            print(self.ciphertext)
        elif voir == "n":
            dechiffrement = input("Ecrivez 1 quand vous le souhaitez pour déchiffrer le mot de passe :")

    def dechiffrage(self):
        plaintext = cipher.decrypt(self.chiffrage.ciphertext)
