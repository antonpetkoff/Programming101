import sys


def cat(filename):
    readFile = open(filename, "r")
    result = readFile.read()
    readFile.close()
    return result


def main():
    print(cat(sys.argv[1]))


if __name__ == '__main__':
    main()
