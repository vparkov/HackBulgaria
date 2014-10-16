def calculate_coins(money):
    money *= 100
    coins = [100, 50, 20, 10, 5, 2, 1]
    answer = {}

    for coin in coins:
        needed_coins = int(money / coin)
        answer[coin] = needed_coins
        money -= coin * needed_coins

    return answer


print(calculate_coins(0.53))
print(calculate_coins(8.94))
