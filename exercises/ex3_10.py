#!/usr/bin/env python3

data = (
    [1, 5, 2, 3, 4],
    [4, 5, 0, 4]
)


def solve(list1, list2):
    '''Find common elements of two given lists.

    Returns a list contains those elements.
    Require: use only lists, and loop.
    '''
    result = []
    for num1 in list2 :
        if num1 in list1 and num1 not in result:
                result.append(num1)

    return result


def main():
    L1, L2 = data
    print(solve(L1, L2))


if __name__ == "__main__":
    main()
