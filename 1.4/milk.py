"""
ID: edward.10
LANG: PYTHON3
TASK: milk
"""


def get_input():
    with open('milk.in', 'r') as f:
        N, M = map(int, f.readline().strip().split())

    return N, M


def get_prices():
    with open('milk.in', 'r') as f:
        _, M = map(int, f.readline().strip().split())

        prices = []
        for _ in range(M):
            P, A = map(int, f.readline().strip().split())
            price = P, A
            prices.append(price)

    return prices


if __name__ == '__main__':
    N, M = get_input()
    prices = get_prices()

    sorted_prices = sorted(prices)

    i = 0
    cost = 0
    while True:
        if N <= 0:
            break

        price, quantity = sorted_prices[i]

        cost += min(quantity, N)*price
        N -= min(quantity, N)

        i += 1

    with open('milk.out', 'w') as f:
        f.write(str(cost) +  '\n')

