
def number_to_list(n):
    number = str(n)
    result = []
    for digit in number:
        result.append(int(digit))
    return result


def main():
    print(number_to_list(123))
    print(number_to_list(99999))
    print(number_to_list(123023))


if __name__ == '__main__':
    main()
