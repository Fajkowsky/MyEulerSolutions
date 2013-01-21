import math

def sumSquare(number):
    sum = 0
    for i in range(1, number + 1):
        sum += math.pow(i, 2)
    return sum
    
def squareSum(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return math.pow(sum, 2)
    
def main():
    number = 100
    print(squareSum(number) - sumSquare(number))

if __name__ == '__main__':
    main()