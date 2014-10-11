
def unique_words_count(arr):
    unique = []
    count = 0
    for word in arr:
        if not word in unique:
            count += 1
            unique.append(word)
    return count


def main():
    print(unique_words_count(["apple", "banana", "apple", "pie"]))
    print(unique_words_count(["python", "python", "python", "ruby"]))
    print(unique_words_count(["HELLO!"] * 10))


if __name__ == '__main__':
    main()
