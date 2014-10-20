import sys


def concat_files(fileNames):
    with open("MEGATRON.txt", "a") as writeFile:
        for i in range(len(fileNames)):
            try:
                with open(fileNames[i], "r") as readFile:
                    writeFile.write(readFile.read())
            except FileNotFoundError:
                raise


def main():
    fileNames = []
    for i in range(1, len(sys.argv)):
        fileNames.append(sys.argv[i])
    concat_files(fileNames)


if __name__ == '__main__':
    main()
