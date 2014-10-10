
def number_to_list(n):
    number = str(n)
    result = []
    for digit in number:
        result.append(int(digit))
    return result
