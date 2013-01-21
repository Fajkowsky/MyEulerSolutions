def isPrime(number):
    i = 2
    if(number <= 1):
        return False
    while(i != number):
        if(number % i == 0): 
            return False
        i += 1
    
    return True

def main():
    number = 0
    while(number != 600851475143):
        if(isPrime(number) and 600851475143 % number == 0):
            print(number)
        number += 1

if __name__ == '__main__':
    main()