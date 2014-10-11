
def count_words(arr):
    result = {}
    for word in arr:
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1
    return result


def main():
    print(count_words(["apple", "banana", "apple", "pie"]))
    print(count_words(["python", "python", "python", "ruby"]))


if __name__ == '__main__':
    main()
