from math import sqrt

#### Fonction secondaire

def isprime(p): 
    """Retourne vrai si le nombre est un npmbre premier""" 
    if p in (0, 1): 
        return False 
    for i in range(2, int(sqrt(p)) + 1): 
        if (p % i == 0): 
            return False
    return True

#### Fonction principale


def main():
    """Fonction permettant d'obtenir puis d'afficher tous les nombres premier jusqu'à 100""" 
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
