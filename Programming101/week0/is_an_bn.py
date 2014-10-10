
def is_an_bn(word):
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
