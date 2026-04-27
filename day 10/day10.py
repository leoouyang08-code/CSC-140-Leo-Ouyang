import random as random

x = []
for i in range(1,1000):
    roll = random.randint(1,6) + random.randint(1,6)
    x.append(roll)

print(sum(x)/len(x))

help(random.choice)