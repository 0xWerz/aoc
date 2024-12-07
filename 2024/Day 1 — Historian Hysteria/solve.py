def solve_part_1():
    pairs = []
    with open("input.txt", "r") as f:
        lines = f.read().strip().split("\n")
        for l in lines:
            pairs.append(list(map(int, l.split("   "))))

    pairs.sort()

    l = [p[0] for p in pairs]
    r = [p[1] for p in pairs]

    l.sort()
    r.sort()

    spairs = list(zip(l, r))

    sol = 0
    for p in spairs:
        sol += abs(p[0] - p[1])

    return sol


def count_occurrences(target, lst):
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count


def solve_part_2():
    pairs = []
    with open("input.txt", "r") as f:
        lines = f.read().strip().split("\n")
        for l in lines:
            pairs.append(list(map(int, l.split("   "))))

    l = [p[0] for p in pairs]
    r = [p[1] for p in pairs]
    c = 0
    sol = 0
    for v in l:
        sol += v * count_occurrences(v, r)

    return sol


if __name__ == "__main__":
    s = solve_part_1()
    s2 = solve_part_2()
    print("Part One solution: ", s)
    print("Part Two solution: ", s2)
