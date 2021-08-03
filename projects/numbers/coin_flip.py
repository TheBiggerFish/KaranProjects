import random

loops = int(input("How many coin flips: "))

heads,tails = 0,0
for _ in range(loops):
    if random.random() < 0.5:
        heads += 1
    else:
        tails += 1

print(f'Heads: {heads}, Tails: {tails}, Ratio (Heads/Tails):{heads/tails}')
