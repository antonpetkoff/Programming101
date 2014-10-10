
def iterations_of_nan_expand(expanded):
    if not expanded.find("Not a Nan"):
        return 0
    return (len(expanded) - 3) // 6
