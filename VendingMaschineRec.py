Coins = {
        500: 1,
        200: 10,
        100: 10,
        50: 0,
        20: 10,
        10: 10,
        5: 1000,
        2: 1000,
        1: 1000
    }
Products = {
    "Cola":120,
    "Sok":150,
    "Wafelek":80,
    "Rogal":200,
    "Orzeszki":170,
    "Baton":140
            }
money = [500,200,100,50,20,10,5,2,1]
def WriteProducts():
    for p, q in Products.items():
        print(p, q, "gr")

def EmptyCoins(): # Jeżeli nie ma jakiegoś nominału w automacie usuwa z listy
    for p in Coins.keys():
        if Coins[p] == 0:
            money.remove(p)

def beginCoins(allCoins,firstCoin,n):
    count = 0
    if allCoins == firstCoin:
        return 1
    for i in range(n):
        allCoins -= firstCoin
        if allCoins > 0:
            count += 1
        else:
            pass
    return count
# funkcja wyliczająca maksymalna liczbe najwiekszych mozliwych nominałow które moga byc uzyte do wydania reszty
def change(n,available_coins,coins_so_far):
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif available_coins == []:
        pass
    else:
        for coin in change(n,available_coins[:],coins_so_far+[available_coins[0]]):
            yield coin
        for coin in change(n,available_coins[1:],coins_so_far):
            yield coin

customerMoney = input('Podaj sumę pieniędzy, które chcesz wrzucić: ')
WriteProducts()
selectProduct = Products.get(input('Wybierz produkt: '))
rest = int(customerMoney) - int(selectProduct)
EmptyCoins()
highestCoin = max(s for s in Coins.keys() if s <= rest if s in money) #znajduje pierwsza najwieksza liczbe mniejsza od reszty
money.remove(highestCoin) #usuwam ją z listy
numberOfCoins = Coins[highestCoin] #ile razy dany nominał wystepuje w automacie
beginCoins(rest,highestCoin,numberOfCoins)

solutions = [s for s in change(rest, money,[highestCoin]*beginCoins(rest,highestCoin,numberOfCoins))]
print("Reszta: ", rest, " = ", min(solutions, key=len), "gr")
