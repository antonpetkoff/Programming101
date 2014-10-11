
def what_is_my_sign(day, month):
    months = [
        ["Capricorn",   20],
        ["Aquarius",    19],
        ["Pisces",      20],
        ["Aries",       20],
        ["Taurus",      21],
        ["Gemini",      21],
        ["Cancer",      22],
        ["Leo",         22],
        ["Virgo",       23],
        ["Libra",       23],
        ["Scorpio",     22],
        ["Sagittarius", 21]
    ]

    if day > months[month-1][1]:
        return months[month][0]
    else:
        return months[month-1][0]


def main():
    print(what_is_my_sign(5, 8))
    print(what_is_my_sign(29, 1))
    print(what_is_my_sign(30, 6))
    print(what_is_my_sign(31, 5))
    print(what_is_my_sign(2, 2))
    print(what_is_my_sign(8, 5))
    print(what_is_my_sign(9, 1))


if __name__ == '__main__':
    main()
