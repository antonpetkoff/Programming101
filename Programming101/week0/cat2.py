import sys


def cat2(filenames):
    result = ""
    for i in range(len(filenames)):
        readFile = open(filenames[i], "r")
        result += readFile.read()
        if i != len(filenames) - 1:
            result += '\n'
        readFile.close()
    return result


def main():
    filenames = []
    for i in range(1, len(sys.argv)):
        filenames.append(sys.argv[i])
    print(cat2(filenames))


if __name__ == '__main__':
    main()
