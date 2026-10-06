"""
ID: edward.10
LANG: PYTHON3
TASK: sprime
"""

# from tqdm import trange


def get_input():
    with open('sprime.in', 'r') as f:
        n = int(f.readline())
        return n


def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True

    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def is_superprime(n):
    while True:
        if n == 0:
            break

        if not is_prime(n):
            return False

        n = int(str(n)[:-1] or 0)

    return True


def get_superprimes(n):
    superprimes = []
    for i in range(10**(n-1), 10**n):
        if is_superprime(i):
            superprimes.append(i)
    return superprimes


if __name__ == '__main__':
    n = get_input()

    superprimes = get_superprimes(n)

    with open('sprime.out', 'w') as f:
        for superprime in superprimes:
            f.write(str(superprime) + '\n')

