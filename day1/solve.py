def solve1(data):
    return sum(data[i] < data[i + 1] for i in range(len(data) - 1))


def solve2(data):
    return sum(data[i] < data[i + 3] for i in range(len(data) - 3))


with open("input", "r") as f:
    data = [line.strip() for line in f]
print(f"part 1: {solve1(data)}, part 2: {solve2(data)}")
