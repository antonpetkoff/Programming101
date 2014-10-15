
class Fraction(object):

    def __init__(self, num, denum):
        self.num = num
        self.denum = denum

    # arithmetic
    def __add__(self, other):
        num = self.num * other.denum + other.num * self.denum
        denum = self.denum * other.denum
        return Fraction(num, denum)

    def __sub__(self, other):
        num = self.num * other.denum - other.num * self.denum
        denum = self.denum * other.denum
        return Fraction(num, denum)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.denum * other.denum)

    def __truediv__(self, other):
        return Fraction(self.num * other.denum, self.denum * other.num)

    # relational
    def __eq__(self, other):
        return self.num / self.denum == other.num / other.denum

    def __gt__(self, other):
        return self.num / self.denum > other.num / other.denum

    def __lt__(self, other):
        return self.num / self.denum < other.num / other.denum

    def __str__(self):
        return "({}, {})".format(self.num, self.denum)

def main():
    a = Fraction(1, 2)
    b = Fraction(3, 5)
    c = Fraction(7, 3)
    d = Fraction(2, 4)
    print(str(a + b))
    print(str(a - b))
    print(str(a * b))
    print(str(a / b))
    print(a > c)
    print(a < c)
    print(a == d)

if __name__ == '__main__':
    main()
