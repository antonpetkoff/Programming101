import copy


class CashDesk(object):

    def __init__(self):
        self.money = {100:0, 50:0, 20:0, 10: 0, 5:0, 2:0, 1:0}

    def take_money(self, money):
        for key in money.keys():
            self.money[key] += money[key]

    def total(self):
        sum = 0
        for key in self.money.keys():
            sum += self.money[key] * key
        return sum

    def can_withdraw_money(self, value):
        money = copy.deepcopy(self.money)
        for key in sorted(money.keys(), reverse=True):
            while money[key] > 0 and value - key >= 0:
                value -= key
                money[key] -= 1
        if value > 0:
            return False
        return True


def main():
    my_cash_desk = CashDesk()
    my_cash_desk.take_money({1:2, 50:1, 20:1})
    my_cash_desk.total()
    print(my_cash_desk.can_withdraw_money(30))
    print(my_cash_desk.can_withdraw_money(71))


if __name__ == '__main__':
    main()
