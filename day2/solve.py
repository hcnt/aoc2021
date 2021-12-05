def solve1(data):
    h = 0
    d = 0

    for line in data:
        type, val = line.split()
        val = int(val)
        if type == "forward":
            h += val
        elif type == "up":
            d -= val
        elif type == "down":
            d += val
    return h * d


def solve2(data):
    h = 0
    d = 0
    aim = 0

    for line in data:
        type, val = line.split()
        val = int(val)
        if type == "forward":
            h += val
            d += aim * val
        elif type == "up":
            aim -= val
        elif type == "down":
            aim += val
    return h * d


with open("input", "r") as f:
    data = [line.strip() for line in f]
print(f"part 1: {solve1(data)}, part 2: {solve2(data)}")
