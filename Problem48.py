#!/usr/bin/env python


def main():
    sume = 0
    for number in range(1, 1001):
        sume += number ** number

    sume = str(sume)
    print sume[-10:]
if __name__ == '__main__':
    main()
