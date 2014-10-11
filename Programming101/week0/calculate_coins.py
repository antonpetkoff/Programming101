
def calculate_coins(sum):
    coins = [1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    index = 0
    result = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    while sum > 0 and index < len(coins):
        if sum - coins[index] >= 0:
            sum -= coins[index]
            sum = round(sum, 2)         # for better precision
            result[int(coins[index]*100)] += 1
        else:
            index += 1
    return result


def main():
    print(calculate_coins(0.53))
    print(calculate_coins(8.94))


if __name__ == '__main__':
    main()
