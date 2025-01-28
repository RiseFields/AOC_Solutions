def part1():
    """
    Part 1:
    Calculate the distance between the pairs of the smallest numbers of two given
    lists
    """
    first = []
    second = []
    with open("day1_input.txt", "r") as f:

        for line in f:
            first.append(line.rstrip().split(" ")[0])
            second.append(line.rstrip().split(" ")[-1])

    first.sort()
    second.sort()

    total_dist = 0
    for a, b in zip(first, second):
        total_dist += abs(int(a) - int(b))

    print(total_dist)


def part2():
    """
    Part 2:
    Calculate the similaryto score:
    Add up the amount of times a number appears in the other list, multiplies by
    itself
    """
    first = []
    second = []
    with open("day1_input.txt", "r") as f:

        for line in f:
            first.append(int(line.rstrip().split(" ")[0]))
            second.append(int(line.rstrip().split(" ")[-1]))

    total_sim = 0

    for a in first:
        total_sim += a * second.count(a)

    print(total_sim)

if __name__ == "__main__":
    part1()
    part2()
