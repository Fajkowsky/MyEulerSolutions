
def main():
    i = 1
    sums = 0
    below = 1000
    while(i < below):
        if(i%3 == 0 or i%5 == 0):
            sums += i
        i += 1
    print(sums)

if __name__ == '__main__':
    main()