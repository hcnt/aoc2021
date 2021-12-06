from collections import defaultdict
from itertools import zip_longest


def solve(data: list, skip_diag: bool) -> int:
    positions: dict = defaultdict(lambda: 0)
    for line in data:
        x, _, y = line.split()
        x, y = tuple(map(int, x.split(","))), tuple(map(int, (y.split(","))))
        if skip_diag and not (x[0] == y[0] or x[1] == y[1]):
            continue
        dir1, dir2 = int(x[0] >= y[0]), int(x[1] >= y[1])
        for i, j in zip_longest(
            range(x[0], y[0] + (-1) ** dir1, (-1) ** dir1),
            range(x[1], y[1] + (-1) ** dir2, (-1) ** dir2),
            fillvalue=x[0] if x[0] == y[0] else x[1],
        ):
            positions[(i, j)] += 1
    return sum(1 for _, v in positions.items() if v > 1)


with open("input", "r") as f:
    data = [line.strip() for line in f]
print(f"part 1: {solve(data, True)}, part 2: {solve(data, False)}")
