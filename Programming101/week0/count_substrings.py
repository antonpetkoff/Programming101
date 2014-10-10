
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
