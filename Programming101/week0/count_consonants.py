
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
