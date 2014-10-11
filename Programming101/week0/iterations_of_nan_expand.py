
def iterations_of_nan_expand(expanded):
    if len(expanded) < 1:
        return 0
    if expanded.find("NaN") == -1:
        return False
    print("result", (len(expanded) - 3) // 6)
    return (len(expanded) - 3) // 6


def main():
    print(iterations_of_nan_expand(""))
    print(iterations_of_nan_expand("Not a NaN"))
    print(iterations_of_nan_expand("Not a Not a Not a Not a \
    Not a Not a Not a Not a Not a Not a NaN"))
    print(iterations_of_nan_expand("Show these people!"))


if __name__ == '__main__':
    main()
