import numpy as np


def solve(data):
    return np.sum(np.abs(data - np.median(data)))


def solve2(data):
    d = {
        i: np.sum(((np.abs(data - i)) * (np.abs(data - i) + 1)) // 2)
        for i in range(np.max(data))
    }
    print(min(d, key=d.get))
    return d[min(d, key=d.get)]


with open("input", "r") as f:
    data = np.array([int(x) for x in f.readline().strip().split(",")])
print(f"part 1: {solve(data)}, part 2: {solve2(data)}")
