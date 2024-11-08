from math import sqrt

#### Fonction secondaire

def isprime(p):
    premier = True
    for i in range(2, int(sqrt(p)) + 1):
        if (p % i == 0):
            premier = False
            break
    return premier
    

#### Fonction principale

def main():
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    main()