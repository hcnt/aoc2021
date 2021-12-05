def solve(data, jump):
    return sum(data[i] < data[i + jump] for i in range(len(data) - jump))


with open("input", "r") as f:
    data = [line.strip() for line in f]
print(f"part 1: {solve(data, 1)}, part 2: {solve(data, 3)}")
