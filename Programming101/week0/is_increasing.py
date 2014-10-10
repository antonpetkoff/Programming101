
def is_increasing(seq):
    if len(seq) < 1:
        return False
    previous = seq[0]
    for i in range(1, len(seq)):
        if int(seq[i]) <= previous:
            return False
        else:
            previous = int(seq[i])
    return True
