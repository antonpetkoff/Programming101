import sys


def cat(filename):
    return open(filename).read()


def main():
    print(cat(sys.argv[1]))


if __name__ == '__main__':
    main()
