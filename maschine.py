import math



def Rest(amount):
    money = [10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
    coins = {
        10: 10,
        5: 10,
        2: 10,
        1: 0,
        0.5: 1,
        0.2: 10,
        0.1: 10,
        0.05: 10,
        0.02: 10,
        0.01: 10
    }
    print('Reszta: %s' % round(amount,2))
    sum = 0
    restMoney = 0
#   amount += 0.005
    while sum != amount and money != []:
        x = money[0]
        money.remove(x)
        if coins[x] != 0:
            if sum + x <= amount:
                n=math.floor((amount - sum)/x)
                print('%s*%s' % (n, x))
                sum += n*x
                restMoney += n
                if x in coins.keys():
                    coins[x] -= 1
        else:
            pass
    print(coins.values())
#    if sum - amount < 0.006:
#        print('Liczba użytych monet: %s' % restMoney)
#    else:
#        print('Nie można wydać reszty')
#    return restMoney

customerMoney = input('Podaj sumę pieniędzy, które chcesz wrzucić: ')

Products = {
    "Cola":1.2,
    "Sok":1.5,
    "Wafelek":0.8,
    "Rogal":2.0,
    "Orzeszki":1.7
            }
print(str(Products), "\n")
selectProduct = Products.get(input('Wybierz produkt: '))

rest = float(customerMoney) - float(selectProduct)

Rest(rest)

