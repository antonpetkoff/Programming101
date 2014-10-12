import sys


def sum_numbers(filename):
    readFile = open(filename, "r")
    numbers = readFile.read().split(" ")
    readFile.close()
    sum = 0
    for number in numbers:
        if len(number) > 0:
            sum += int(number)
    return sum


def main():
    print(sum_numbers(sys.argv[1]))


if __name__ == '__main__':
    main()
