#!/usr/bin/env python3


def solve(N):
    '''
    What is the sum of the digits of the number `2**1000`?
    https://projecteuler.net/problem=16

    Must: use list comprehension
    Tips: list comprehension always create new list
    '''
    result = sum([int(i) for i in list(str(2**N))])


    return result


def main():
    print(solve(1000))


if __name__ == "__main__":
    main()
