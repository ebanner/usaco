"""
ID: edward.10
LANG: PYTHON3
TASK: pprime
"""

from tqdm import trange

def get_input():
    with open('pprime.in', 'r') as f:
        return map(int, f.readline().split())


def get_factors(n):
    factors = []
    for m in range(1, n+1):
        if n % m == 0:
            factors.append(m)
    return factors


def is_prime(n):
    factors = get_factors(n)
    return len(factors) == 2


def is_palindrome(n):
    n_ = str(n)
    return n_ == n_[::-1]


if __name__ == '__main__':
    a, b = get_input()

    prime_palindromes = []
    for n in trange(a, b+1):
        if is_palindrome(n) and is_prime(n):
            prime_palindromes.append(n)

    with open('pprime.out', 'w') as f:
        for prime_palindrome in prime_palindromes:
            f.write((str(prime_palindrome) + '\n'))

