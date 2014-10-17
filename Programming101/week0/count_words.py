
def count_words(arr):
    result = {}
    for word in arr:
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1
    return result
