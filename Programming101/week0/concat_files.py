import sys


def concat_files(filenames):
    writeFile = open("MEGATRON.txt", "a")
    for i in range(len(filenames)):
        readFile = open(filenames[i], "r")
        writeFile.write(readFile.read() + '\n')
        readFile.close()
    writeFile.close()


def main():
    filenames = []
    for i in range(1, len(sys.argv)):
        filenames.append(sys.argv[i])
    concat_files(filenames)


if __name__ == '__main__':
    main()
