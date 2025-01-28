import re


def part1():
    text = []
    count = 0
    with open("day4_input.txt", "r") as f:
        for line in f:
            text.append(line.rstrip())

    for line in text:
        count += len(re.findall(r"XMAS", line))
        count += len(re.findall(r"SAMX", line))

    textv = ["".join(i) for i in list(zip(*text))]
    for line in textv:
        count += len(re.findall(r"XMAS", line))
        count += len(re.findall(r"SAMX", line))

    for i in range(len(text) - 3):
        for j in range(len(text[i]) - 3):
            if f"{text[i][j]}{text[i+1][j+1]}{text[i+2][j+2]}{text[i+3][j+3]}" in ("XMAS", "SAMX"):
                count += 1
            if f"{text[i][j+3]}{text[i+1][j+2]}{text[i+2][j+1]}{text[i+3][j]}" in ("XMAS", "SAMX"):
                count += 1

    return count


def part2():
    text = []
    count = 0
    with open("day4_input.txt", "r") as f:
        for line in f:
            text.append(list(line.rstrip()))

    for i in range(len(text) - 2):
        for j in range(len(text[i]) - 2):
            if ("".join((text[i][j], text[i+1][j+1], text[i+2][j+2])) in ("MAS", "SAM") and
                    "".join((text[i][j+2], text[i+1][j+1], text[i+2][j])) in ("MAS", "SAM")):
                count += 1
    return count


if __name__ == "__main__":
    print(part1())
    print(part2())
    # test = ["abcde", "fghij", "klmno", "pqrst"]
    # print(test)
    # print(*test)
    # print(list(zip(*test)))
    # print(["".join(i) for i in list(zip(*test))])
    # for i in range(len(test) - 2):
    #     for j in range(len(test[i]) - 2):
    #         print(f"{test[i][j]}{test[i+1][j+1]}{test[i+2][j+2]}")
    #         print(f"{test[i][j+2]}{test[i+1][j+1]}{test[i+2][j]}")
