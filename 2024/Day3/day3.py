import re


def part1():
    """
    Part 1
    Find all complete "mul(X,Y)" in a text, where X and Y are 1-3 digit numbers
    Add up the result of all multiplications
    """

    total = 0
    with open("day3_input.txt", "r") as f:
        for line in f:
            muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line.rstrip())
            total += sum([int(a) * int(b)
                         for a, b in [re.findall(r"\d{1,3}", i) for i in muls]])
    return total


def part2():
    """
    Part 2
    Find all complete "mul(X,Y)" in a text, where X and Y are 1-3 digit numbers
    Add up the result of all multiplications
    Don't accept mul() which are after a don't()
    Accept mul() which are after a do()
    """

    total = 0
    text = ""
    with open("day3_input.txt", "r") as f:
        for line in f:
            text += line.rstrip()

    filtered = re.findall(
        r"(?<=^....|do\(\))(.*?)(?=$|don't\(\))", text)
    print(filtered)
    muls = [re.findall(r"mul\(\d{1,3},\d{1,3}\)", i) for i in filtered]
    for section in muls:
        total += sum([int(a) * int(b)
                      for a, b in [re.findall(r"\d{1,3}", i) for i in section]])
    return total


if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())
