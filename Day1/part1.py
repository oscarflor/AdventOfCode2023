"""AOC Day 1 Part 1"""

def get_input():
    """Returns content of input.txt"""
    with open("Day1/input.txt", 'r', encoding="utf-8") as f:
        data = f.readlines()
    return data

def get_firstlast_digits(line: str) -> (str, str):
    """finds the first and last digits of a string"""
    first = ''
    last = ''
    # search forward for a digit
    for char in line:
        if char.isnumeric():
            first = char
            break
    # search backwards for a digit
    for char in reversed(line):
        if char.isnumeric():
            last = char
            break

    return (first, last)

def main() -> None:
    """Main function"""
    data = get_input()
    sum_of_values = 0
    for line in data:
        first, last = get_firstlast_digits(line)
        calibration_value = int(first + last)
        sum_of_values += calibration_value

    print(sum_of_values)


if __name__ == "__main__":
    main()
