
def is_vowel(letter):
    vowels = "aeoiuy"
    letter = str(letter).lower()
    for vowel in vowels:
        if letter == vowel:
            return True
    return False


def count_vowels(str):
    count = 0
    for letter in str:
        if is_vowel(letter):
            count += 1
    return count
