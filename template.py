"""AOC Day # Part #"""

def get_input():
    """Returns content of input.txt"""
    with open("Day#/input.txt", 'r', encoding="utf-8") as f:
        data = f.readlines()
    return data

def main():
    """Main function"""
    data = get_input()
    return data

if __name__ == "__main__":
    main()
