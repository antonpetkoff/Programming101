
def is_consonant(letter):
    consonants = "bcdfghjklmnpqrstvwxz"
    letter = str(letter).lower()
    for consonant in consonants:
        if letter == consonant:
            return True
    return False


def count_consonants(str):
    count = 0
    for letter in str:
        if is_consonant(letter):
            count += 1
    return count


def main():
    print(count_consonants("Python"))
    print(count_consonants("Theistareykjarbunga"))
    print(count_consonants("grrrrgh!"))
    print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_consonants("A nice day to code!"))


if __name__ == '__main__':
    main()
