
def isPalindrome(number):
    if(number % 11 == 0):
        stringNumber = str(number)
        tmp1 = stringNumber[len(stringNumber)/2:]
        tmp2 = stringNumber[:len(stringNumber)/2]
        if(tmp1 == tmp2[::-1]):
            return True
    else:
        return False

def main():
    firstMul = 999
    secondMul = 999
    max = 0
    for i in range(1, firstMul):
        for j in range(1, secondMul):
            mul = i * j
            if(isPalindrome(mul) and max < mul):
                max = mul 
                print(mul, " ", i, " X ", j)
            
            
        
if __name__ == '__main__':
    main()