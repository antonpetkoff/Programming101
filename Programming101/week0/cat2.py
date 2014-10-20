import sys


def cat2(fileNames):
    result = ""
    for i in range(len(fileNames)):
        try:
            with open(fileNames[i], "r") as readFile:
                result += readFile.read()
        except FileNotFoundError:
            raise
    return result


def main():
    fileNames = []
    for i in range(1, len(sys.argv)):
        fileNames.append(sys.argv[i])
    print(cat2(fileNames))


if __name__ == '__main__':
    main()
