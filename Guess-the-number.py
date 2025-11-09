"""simpelt "Guess The Number" spil"""

# import modul
import random


# liste af tal
tal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# variabler
tal_input = int(input("Gæt et tal, og se om det er rigtigt: "))
skab_tal = random.choice(tal)


def sammenlign_tal(skab_tal, tal_input):
    if skab_tal == tal_input:
        print(f"Du gættede rigtigt, da jeg valgt {skab_tal}")
    else:
        print(f"Du gættede forkert, da jeg valgt {skab_tal}")


# kald funktion
sammenlign_tal(skab_tal, tal_input)
