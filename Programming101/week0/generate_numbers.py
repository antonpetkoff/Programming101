import sys
from random import randint


def generate_numbers(fileName, n):
    writeFile = open(fileName, "w")
    for i in range(n):
        writeFile.write(str(randint(1, 1000)) + " ")
    writeFile.close()


def main():
    generate_numbers(sys.argv[1], int(sys.argv[2]))


if __name__ == '__main__':
    main()
