import random

dice = ["9", "10", "J", "Q", "K", "A"]

def make_sample_space(lst: list) -> list[tuple]:
    result = []
    for i in lst:
        for j in lst:
            result.append((i,j))
    return result
# or sample_space = [(x,y) for x in dice for y in dice]
sample = make_sample_space(dice)

def simulate_throws_from_sample_space(sample_space: list[tuple], n_throws: int) -> list[tuple]:
    return random.choices(sample_space, k=n_throws)

throws = simulate_throws_from_sample_space(sample, 10)

def simulate_throws(data, n_throws: int):
    return [tuple(random.choices(data, k=2)) for _ in range(n_throws)]

throws_2 = simulate_throws(dice, 10)
