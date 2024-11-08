"""
Ce module contient une fonction pour vérifier si un nombre est premier,
ainsi qu'une fonction principale pour afficher les nombres premiers jusqu'à 100.
"""

from math import sqrt

# Fonction secondaire
# La fonction isPrime() permet de renvoyer si le nbr en paramètre est premier
def isprime(p):
    """
    Détermine si un nombre est premier.
    
    Paramètre:
    p (int): Le nombre entier à vérifier.
    
    Retourne:
    bool: True si le nombre est premier, False sinon.
    """

    if p == 1:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

# Fonction principale
# Fonction principale qui fait tourner le code
def main():
    """
    Affiche tous les nombres premiers de 0 à 99.
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    main()
