def isPrime(number):
    if(number <= 1):
        return False
    elif(number == 2):
        return True
    else:
        for i in range(3,number,2):
            if(number % i == 0):
                return False
    return True
    

def main():
    i,j = 0,0
    loop = True
    while(loop):
        if(isPrime(i)): 
            j += 1
            if(j == 1000):
                print(i)
                loop = False
        i += 1
          
    

if __name__ == '__main__':
    main()