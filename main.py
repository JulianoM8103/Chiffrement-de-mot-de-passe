from cryptography.fernet import Fernet
import os
import time
from random import randint
from rich.progress import track

key = Fernet.generate_key()
fernet = Fernet(key)

class Main:
    def menu(self):
        os.system("cls")

        print("\n\nMENU PRINCIPAL")
        print("\n-----------------------------------------------")

        print("\nTapez 1 pour chiffrer un mot de passe, 2 pour déchiffrer un mot de passe et 3 pour quitter")
        choix = input("\n>>>")

        if choix == "1":
            root = Chiffrage()
            root.ask1()
        elif choix == "2":
            root = Déchiffrage()
            root.ask2()
        elif choix == "3":
            os.system("cls")
            exit()
        else:
            print("Choix incorrect, veuillez recommencer")
            time.sleep(1)
            root = Main()
            root.menu()

class Chiffrage:
    def ask1(self):
        os.system("cls")

        self.time = randint(1,7)

        print("\n\nCHIFFRAGE DE MOTS DE PASSE")
        print("\n-----------------------------------------------")
        password = input("\n Quelle est le mot de passe que tu souhaite chiffrer ? \n\n>>>")
        password = bytes(password, 'utf-8')

        ciphertext = fernet.encrypt(password)

        for i in track(range(int(self.time)), description="Cryptage en cours..."):
            time.sleep(1)

        os.system("cls")


        print(f"\n\n Voici le mot de passe chiffré : \n", ciphertext)
        print("Copie uniquement ce qui est entre les guillements (les caractères aléatoires)")

        choix = input("\n\nPour revenir à l'écran principal, tapez 1. Pour quitter, tapez 2\n\n>>>")

        if choix == "1":
            time.sleep(1)
            root = Main()
            root.menu()
        elif choix == "2":
            exit()
            


class Déchiffrage:
    def ask2(self):
        os.system("cls")

        print("\n\nDECHIFFRAGE DE MOTS DE PASSE")
        print("\n-----------------------------------------------")
        password = input("\n Rentre le mot de passe chiffrer \n\n>>>")

        plain_text = fernet.decrypt(password).decode()

        os.system("cls")

        print("Le mot de passe est :", plain_text)

root = Main()
root.menu()
