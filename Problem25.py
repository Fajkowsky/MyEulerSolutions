#!/usr/bin/env python


def main():
    first = 1
    second = 1
    value = 0
    term = 2
    while True:
        value = first + second
        second = first
        first = value
        term += 1
        if len(str(value)) > 999:
            break
    print term

if __name__ == '__main__':
    main()
