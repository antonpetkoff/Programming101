
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
