import sys


def wc(command, filename):
    try:
        with open(filename, "r") as readFile:
            if command == "chars":
                return len(readFile.read())
            elif command == "words":
                text = readFile.read().replace("\n", " ")
                words = text.split(" ")
                wordsCount = 0
                for word in words:
                    if word != "":
                        wordsCount += 1
                return wordsCount
            elif command == "lines":
                return len(readFile.readlines())
            else:
                return "Invalid command!"
    except FileNotFoundError:
        raise


def main():
    print(wc(sys.argv[1], sys.argv[2]))


if __name__ == '__main__':
    main()
