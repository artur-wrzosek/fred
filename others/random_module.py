import random

# setting a constant seed generates deterministic random numbers
random.seed()
for _ in range(5):
    print(random.random())

for _ in range(5):
    print(random.randrange(1,6))

for _ in range(5):
    print(random.gauss(0,1))

lst = [4, 3, 6, 7, 1, 8, 9]
# shuffle in place on mutable sequences
random.shuffle(lst)
print(lst)
# choices - with replacements
print(random.choices(lst, k=5))
# sample - without replacements
print(random.sample(lst, k=3))