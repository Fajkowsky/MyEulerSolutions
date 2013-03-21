
def main():
    one = 1
    two = 2
    i = 0
    before = 1
    now = 2
    fibb = 0
    sum = 0
    while(i < 4000000-2):
        fibb = now + before
        before = now
        now = fibb
        i += 1
        if(fibb%2 == 0):
            sum += fibb
       
    print(sum)
    
    
if __name__ == '__main__':
    main()