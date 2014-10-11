
def is_an_bn(word):
    if len(word) == 0:
        return True
    if len(word) < 2:
        return False
    if len(word) % 2 != 0:
        return False
    for i in range(len(word)//2):
        if word[i] != "a":
            return False
        if word[len(word)-i-1] != "b":
            return False
    return True


def main():
    print(is_an_bn(""))
    print(is_an_bn("rado"))
    print(is_an_bn("aaabb"))
    print(is_an_bn("aaabbb"))
    print(is_an_bn("aabbaabb"))
    print(is_an_bn("bbbaaa"))
    print(is_an_bn("aaaaabbbbb"))


if __name__ == '__main__':
    main()
