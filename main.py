import random
import math


def menu():
    print("########################")
    print("### MENU JEU DE MATH ###")
    print("########################")

    debut_menu = 0
    nb_max = 0
    nb_question = 0

    while debut_menu == 0:
        print("Tapez 0 pour quitter le jeu")
        print("Tapez 1 pour le niveau débutant")
        print("Tapez 2 pour le niveau intermédiaire")
        print("Tapez 3 pour le niveau expert !")

        try:
            debut_menu = int(input("Quel est votre choix ?"))
        except ValueError:
            print("Veuillez saisir un nombre valide.")
            continue

        if debut_menu == 0:
            break

        elif debut_menu == 1:
            nb_max = 10
            nb_question = 5

        elif debut_menu == 2:
            nb_max = 20
            nb_question = 10

        elif debut_menu == 3:
            nb_max = 50
            nb_question = 20

    return nb_question, nb_max


# Appel de la fonction menu pour obtenir les valeurs de nb_question et nb_max
nb_question, nb_max = menu()

if nb_question == 0 and nb_max == 0:
    print("Vous avez quitté le jeu.")
else:
    print("Nombre de questions :", nb_question)
    print("Nombre maximum :", nb_max)


def poser_question(nb_min, nb_max):
    a = random.randint(nb_min, nb_max)
    b = random.randint(nb_min, nb_max)
    operation = random.choice(["+", "*"])

    if operation == "+":
        reponse_int = None

        while reponse_int is None:
            try:
                reponse_str = input(f"{a} + {b} = ? ")
                reponse_int = int(reponse_str)
            except ValueError:
                print("Veuillez saisir un nombre valide.")

        if reponse_int == a + b:
            print()
            print("Réponse correcte")
            return 1
        else:
            print()
            print("Réponse incorrecte")
            return 0

    elif operation == "*":
        reponse_int = None

        while reponse_int is None:
            try:
                reponse_str = input(f"{a} * {b} = ? ")
                reponse_int = int(reponse_str)
            except ValueError:
                print("Veuillez saisir un nombre valide.")

        if reponse_int == a * b:
            print()
            print("Réponse correcte")
            return 1
        else:
            print()
            print("Réponse incorrecte")
            return 0


score_total = 0

if nb_question != 0:
    for i in range(nb_question):
        print()
        print(f"Question {i+1}/{nb_question}")
        print()
        score_total += poser_question(1, nb_max)


# Calcul de la moyenne en pourcentage et arrondi au supérieur
moyenne = math.ceil((score_total / nb_question) * 100)

print()
print("Félicitations, vous avez terminé toutes les questions !")
print("Votre score total :", score_total)
print("Moyenne des réponses correctes :", "{}%".format(moyenne))
