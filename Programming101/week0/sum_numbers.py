import sys


def sum_numbers(fileName):
    sum = 0
    try:
        with open(fileName, "r") as readFile:
            numbers = readFile.read().split(" ")
            for number in numbers:
                if len(number) > 0:
                    sum += int(number)
    except FileNotFoundError:
        return "File {} not found!".format(fileName)
    return sum


def main():
    print(sum_numbers(sys.argv[1]))


if __name__ == '__main__':
    main()
