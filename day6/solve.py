from collections import Counter


def solve(data, n):
    ct = Counter(data)
    data_ct = [ct[i] for i in range(9)]
    for _ in range(n):
        data_ct = data_ct[1:] + data_ct[:1]
        data_ct[6] += data_ct[8]

    return sum(data_ct)


with open("input", "r") as f:
    data = [int(x) for x in f.readline().strip().split(",")]
print(f"part 1: {solve(data, 80)}, part 2: {solve(data, 256)}")
