
def unique_words_count(arr):
    unique = []
    count = 0
    for word in arr:
        if not word in unique:
            count += 1
            unique.append(word)
    return count
