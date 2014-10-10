import sys


def cat(filename):
    my_file = open(filename)
    contents = my_file.read()
    return contents


def main():
    print(cat(sys.argv[1]))


if __name__ == '__main__':
    main()
