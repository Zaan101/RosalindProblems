from itertools import permutations
import math

data = 5
real = ''
for i in range(1,data+1):
    real = real + str(i)

perms = [''.join(p) for p in permutations(real)]


with open("output.txt", "a") as f:
    print(math.factorial(data),file=f)
    for i in perms:
        print(' '.join(i),file=f)
