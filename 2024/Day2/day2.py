def check_safe(numbers):
    # Check descending row
    if numbers[0] > numbers[1]:
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i+1]:
                return i
            if numbers[i] - numbers[i+1] > 3:
                return i
            if numbers[i] == numbers[i+1]:
                return i
        return True
    # Check ascending row
    if numbers[0] < numbers[1]:
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                return i
            if numbers[i+1] - numbers[i] > 3:
                return i
            if numbers[i + 1] == numbers[i]:
                return i
        return True
    # If the first 2 are equal, not safe
    if numbers[0] == numbers[1]:
        return 0


def check_safe_demper(numbers):
    result = check_safe(numbers)
    # Check if the code is safe by removing the wrong number
    # Could be the number before or after aswell
    if result is not True:
        if check_safe(numbers[:result] + numbers[result+1:]) is True:
            return True
        if check_safe(numbers[:result-1] + numbers[result:]) is True:
            return True
        if check_safe(numbers[:result+1] + numbers[result+2:]) is True:
            return True
    return result


def part1():
    """
    Part 1
    A code (row of numbers) is safe if they are all ascending or descending,
    with at most 3 difference between two numbers
    """
    safe = 0
    with open("day2_input.txt", "r") as f:
        for line in f:
            numbers = [int(i) for i in line.rstrip().split(" ")]
            if check_safe(numbers) is True:
                safe += 1
    print("Safe levels: ", safe)
    return safe


def part2():
    """
    Part 2
    One of the numbers in the codes can be wrong for it to be still safe
    """
    safe = 0
    with open("day2_input.txt", "r") as f:
        for line in f:
            numbers = [int(i) for i in line.rstrip().split(" ")]
            if check_safe_demper(numbers) is True:
                # print("Safe with demper: ", numbers)
                safe += 1
            # else:
            #     # print("UNSAFE with demper: ", numbers)
    print("Safe levels with demper: ", safe)
    return safe


if __name__ == "__main__":
    part1()
    part2()
