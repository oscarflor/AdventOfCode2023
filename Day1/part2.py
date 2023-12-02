"""AOC Day 1 Part 1"""

def get_input():
    """Returns content of input.txt"""
    with open("Day1/input.txt", 'r', encoding="utf-8") as f:
        data = f.readlines()
    return data

def get_firstlast_digits(line: str) -> (str, str):
    """finds the first and last digits of a string, words included like one, two, etc"""
    line = line.strip()
    first_digit = ''
    first_digit_index = 0
    last_digit = ''
    last_digit_index = len(line) - 1
    words = {'one': "1", 'two': "2", 'three': "3", 'four': "4", 'five': "5",
            'six': "6", 'seven': "7", 'eight': "8", 'nine': "9"}

    # search forward for a digit
    for i, char in enumerate(line):
        if char.isnumeric():
            first_digit = char
            first_digit_index = i
            break

    # search backwards for a digit
    for i, char in enumerate(reversed(line)):
        if char.isnumeric():
            last_digit = char
            last_digit_index -= i
            break

    # search for word versions of digits in the line
    for word, numerical_version_of_word in words.items():
        index_of_first_word = line.find(word)
        index_of_last_word = line.rfind(word) # reverse find
        if index_of_first_word != -1 and index_of_first_word < first_digit_index:
            first_digit = numerical_version_of_word
            first_digit_index = index_of_first_word
        if index_of_last_word != -1 and index_of_last_word > last_digit_index:
            last_digit = numerical_version_of_word
            last_digit_index = index_of_last_word

    return (first_digit, last_digit)

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
