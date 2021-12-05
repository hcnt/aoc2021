def load():
    with open("input", "r") as f:
        return [line.strip() for line in f]


position_count = []


def solve1(data):
    line1 = data[0]
    for c in line1:
        if c == "1":
            position_count.append(1)
        if c == "0":
            position_count.append(0)
    for i in range(1, len(data)):
        for i, c in enumerate(data[i]):
            position_count[i] += 1 if c == "1" else 0
    print(position_count)
    print(len(data))
    print(1816 * 2279)  # xD


def calc_pos_count(vals):
    positions = [0 for i in range(len(vals[0]))]
    for val in vals:
        for i, c in enumerate(val):
            positions[i] += 1 if c == "1" else 0
    return positions


def solve2(data):
    i = 0
    best_string = ""
    while True:
        position_count = calc_pos_count(data)
        print(position_count)
        best_string += "1" if position_count[i] >= len(data) / 2 else "0"
        data = [val for val in data if val.startswith(best_string)]
        print(best_string)
        print(len(data))
        if len(data) == 1:
            print(int(data[0], 2))
            break
        i += 1


def main():
    data = load()
    # print(solve1(data))
    print(solve2(data))


if __name__ == "__main__":
    main()
