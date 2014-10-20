import sys


def cat2(fileNames):
    result = ""
    for i in range(len(fileNames)):
        try:
            with open(fileNames[i], "r") as readFile:
                result += readFile.read()
                if i != len(fileNames) - 1:     # split with newlines
                    result += '\n'
        except FileNotFoundError:
            return "File {} not found!".format(fileNames[i])
    return result


def main():
    fileNames = []
    for i in range(1, len(sys.argv)):
        fileNames.append(sys.argv[i])
    print(cat2(fileNames))


if __name__ == '__main__':
    main()
