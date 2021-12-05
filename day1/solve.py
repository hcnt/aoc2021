def load():
    with open("input", "r") as f:
        return [int(line.strip()) for line in f]


def solve1(data):
    return sum(data[i] < data[i + 1] for i in range(len(data) - 1))


def solve2(data):
    return sum(data[i] < data[i + 3] for i in range(len(data) - 3))


def main():
    data = load()
    print(solve1(data))
    print(solve2(data))


if __name__ == "__main__":
    main()
