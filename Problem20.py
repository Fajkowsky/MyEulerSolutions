#!/usr/bin/env python

def main():
    value = 1
    sume = 0
    for number in range(1,101):
        value *= number

    value = str(value)
    for number in value:
        sume += int(number)

    print sume
if __name__ == '__main__':
    main()