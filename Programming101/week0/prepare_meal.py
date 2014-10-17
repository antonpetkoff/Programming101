
def prepare_meal(number):
    if number < 1:
        return ""
    if number % 3 == 0:
        n = 1
        while number % 3**n == 0:
            n += 1
        result = "spam " * (n-1)

        if number % 5 == 0:
            result += "and eggs"

        return result.strip()
    elif number % 5 == 0:
        return "eggs"
    else:
        return ""
