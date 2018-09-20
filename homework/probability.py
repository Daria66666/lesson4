import random


def prob(n):
    even = 0
    for x in range(n):
        if random.randint(1, 100) % 2 == 0:
            even += 1
    return round(even/n*100)
