"""
ID: edward.10
LANG: PYTHON3
TASK: pprime
"""

import math


def get_input():
    with open('pprime.in', 'r') as f:
        return map(int, f.readline().split())


def is_prime(n):
    for d in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def is_palindrome(n):
    n_ = str(n)
    return n_ == n_[::-1]


def get_palindromes():
    palindromes = set()

    """

    a

    """
    for a in range(0, 9+1):
        palindromes.add((a,))

    """

    aa

    """
    for a in range(0, 9+1):
        if a == 0:
            continue
        palindromes.add((a, a))

    """

    bab

    """
    for a in range(0, 9+1):
        for b in range(0, 10):
            if b == 0:
                continue
            palindromes.add((b, a, b))

    """

    baab

    """
    for a in range(0, 9+1):
        for b in range(0, 10):
            if b == 0:
                continue
            palindromes.add((b, a, a, b))

    """

    cbabc

    """
    for a in range(0, 9+1):
        for b in range(0, 10):
            for c in range(0, 10):
                if c == 0:
                    continue
                palindromes.add((c, b, a, b, c))

    """

    cbaabc

    """
    for a in range(0, 9+1):
        for b in range(0, 10):
            for c in range(0, 10):
                if c == 0:
                    continue
                palindromes.add((c, b, a, a, b, c))

    """

    dcbabcd

    """
    for a in range(0, 9+1):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    if d == 0:
                        continue
                    palindromes.add((d, c, b, a, b, c, d))

    """

    dcbaabcd

    """
    for a in range(0, 9+1):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    if d == 0:
                        continue
                    palindromes.add((d, c, b, a, a, b, c, d))

    return palindromes


def get_number(nums):
    return sum(d*10**i for i, d in enumerate(reversed(nums)))


if __name__ == '__main__':
    a, b = get_input()

    palindromes = get_palindromes()

    prime_palindromes = []
    for palindrome in palindromes:
        num = get_number(palindrome)
        if is_prime(num):
            prime_palindromes.append(num)

    prime_palindromes = sorted(
        prime_palindrome
            for prime_palindrome in prime_palindromes
            if a <= prime_palindrome <= b
    )

    with open('pprime.out', 'w') as f:
        for prime_palindrome in prime_palindromes:
            f.write((str(prime_palindrome) + '\n'))

