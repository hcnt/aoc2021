def solve_board(ops, board):
    b1 = [[False for _ in range(5)] for _ in range(5)]
    b2 = [[False for _ in range(5)] for _ in range(5)]

    for k, op in enumerate(ops):
        for i in range(5):
            for j in range(5):
                if board[i][j] == op:
                    b1[i][j] = True
                    b2[j][i] = True
                    if any(all(x) for x in b1) or any(all(x) for x in b2):
                        return k, board, b1


def solve(data, func):
    ops = data[0].split(",")
    num, vals, flags = func(
        (
            solve_board(ops, [line.split() for line in data[i : i + 5]])
            for i in range(2, len(data), 6)
        ),
        key=lambda x: x[0],
    )
    return int(ops[num]) * sum(
        sum(int(x) for x, flag in zip(row, flags_row) if not flag)
        for row, flags_row in zip(vals, flags)
    )


with open("input", "r") as f:
    data = [line.strip() for line in f]
print(f"part 1: {solve(data, min)}, part 2: {solve(data, max)}")
