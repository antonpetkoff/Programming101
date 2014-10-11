
def biggest_difference(arr):
    minimum = min(arr)
    maximum = max(arr)
    return minimum - maximum


def main():
    print(biggest_difference([1, 2]))
    print(biggest_difference([1, 2, 3, 4, 5]))
    print(biggest_difference([-10, -9, -1]))
    print(biggest_difference(range(100)))


if __name__ == '__main__':
    main()
