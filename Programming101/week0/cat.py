import sys


def cat(filename):
    result = ""
    try:
        with open(filename, "r") as readFile:
            result = readFile.read()
    except FileNotFoundError:
        return "File {} not found!".format(filename)
    return result


def main():
    print(cat(sys.argv[1]))


if __name__ == '__main__':
    main()
