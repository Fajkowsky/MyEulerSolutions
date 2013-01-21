import math
from decimal import *
#Stworzenie listy z liczbami pierwszymi
#Sprawdzenie najwiekszego mnozenia w przedziale
#Mnozenie unikalnych wartosci
def isPrime(number):
    if(number <=1): 
        return False
    for i in range(2, number):
        if(number % i == 0):
            return False
    return True
    
def main():
    rangeNumber = 20
    awnser = 1
    primeList = list()
    #Tworzenie listy z liczbami pierwszymi
    for i in range(1,rangeNumber + 1):
        if(isPrime(i)) : primeList.append(i)
    #Sprawdzenie ile razy dana liczba pierwsza miesci sie w podanym zakresie
    #Tyle ile razy sie miesci tyle podnosimy do potegi i mnozymy z pozostalymi
    #To jest najmniejszy iloczyn liczb podzielnych przez 20
    for i in primeList:
        awnser *= math.pow(i,int(math.pow(rangeNumber, 1/Decimal(i))))
    print(int(awnser))
    
if __name__ == '__main__':
    main()
