#!/usr/bin/env python
import math


def main():
    
    for a in range(0,100):
        for b in range(0,100):
            for c in range(0,100):
                if(a+b+c == 1000) and (a<b<c):
                    print a*b*c
                    break
                print a,b,c

if __name__ == '__main__':
    main()
