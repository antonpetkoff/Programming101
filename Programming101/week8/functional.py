
def compose(f, g):
    return lambda x: f(g(x))


def compose_all(functions):
    result = compose(functions[0], functions[1])
    functions = functions[2:]

    for f in functions:
        functions = compose(result, f)     # reads funcitons from right to left

    return result
