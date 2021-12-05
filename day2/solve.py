def load():
    with open("input", "r") as f:
        return [line.strip() for line in f]


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


def main():
    data = load()
    print(solve1(data))
    print(solve2(data))


if __name__ == "__main__":
    main()
