
def count_substrings(haystack, needle):
    n = len(haystack)
    k = len(needle)
    i = count = 0
    while(i < n - k + 1):
        if haystack[i:i+k] == needle:
            count += 1
            i += k
        else:
            i += 1
    return count


def main():
    print(count_substrings("This is a test string", "is"))
    print(count_substrings("babababa", "baba"))
    print(count_substrings("Python is an awesome language to program in!", "o"))
    print(count_substrings("We have nothing in common!", "really?"))
    print(count_substrings("This is this and that is this", "this"))


if __name__ == '__main__':
    main()
