import sys


def cat2(filenames):
    result = ""
    for i in range(len(filenames)):
        result += open(filenames[i], "r").read()
        if i != len(filenames) - 1:
            result += '\n'
    return result


def main():
    filenames = []
    for i in range(1, len(sys.argv)):
        filenames.append(sys.argv[i])
    print(cat2(filenames))


if __name__ == '__main__':
    main()
