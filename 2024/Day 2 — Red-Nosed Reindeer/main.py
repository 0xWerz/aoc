def solve_part_1():
    reports = []
    with open("example.txt", "r") as f:
        lines = f.read().strip().split("\n")
        for l in lines:
            reports.append(list(map(int, l.split(" "))))

    safe_reports_num = 0

    for r in reports:
        is_increasing = True
        is_decreasing = True

        for i in range(len(r) - 1):
            if r[i] >= r[i + 1]:
                is_increasing = False
            if r[i] <= r[i + 1]:
                is_decreasing = False

        is_safe = True
        for i in range(len(r) - 1):
            difference = abs(r[i] - r[i + 1])
            if not (1 <= difference <= 3):
                is_safe = False
                break

        if (is_increasing or is_decreasing) and is_safe:
            safe_reports_num += 1

    return safe_reports_num


def solve_part_2():
    reports = []
    with open("example.txt", "r") as f:
        lines = f.read().strip().split("\n")
        for l in lines:
            reports.append(list(map(int, l.split(" "))))

    safe_reports_num = 0
    for r in reports:
        is_increasing = True
        is_decreasing = True
        for i in range(len(r) - 1):
            if r[i] >= r[i + 1]:
                is_increasing = False
            if r[i] <= r[i + 1]:
                is_decreasing = False

        is_safe = True
        for i in range(len(r) - 1):
            difference = abs(r[i] - r[i + 1])
            if not (1 <= difference <= 3):
                is_safe = False
                break

        if (is_increasing or is_decreasing) and is_safe:
            safe_reports_num += 1
            continue

        # PART TWO
        for skip_idx in range(len(r)):
            modified_r = r[:skip_idx] + r[skip_idx + 1 :]

            is_increasing = True
            is_decreasing = True
            for i in range(len(modified_r) - 1):
                if modified_r[i] >= modified_r[i + 1]:
                    is_increasing = False
                if modified_r[i] <= modified_r[i + 1]:
                    is_decreasing = False

            is_safe = True
            for i in range(len(modified_r) - 1):
                difference = abs(modified_r[i] - modified_r[i + 1])
                if not (1 <= difference <= 3):
                    is_safe = False
                    break

            if (is_increasing or is_decreasing) and is_safe:
                safe_reports_num += 1
                break

    return safe_reports_num


if __name__ == "__main__":
    s = solve_part_1()
    s2 = solve_part_2()
    print("Part One solution: ", s)
    print("Part Two solution: ", s2)
