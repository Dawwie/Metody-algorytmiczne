Coins = {
        500: 10,
        200: 10,
        100: 10,
        50: 2,
        20: 0,
        10: 10,
        5: 10,
        2: 10,
        1: 10
    }
Products = {
    "Cola":120,
    "Sok":150,
    "Wafelek":80,
    "Rogal":200,
    "Orzeszki":170
            }
money = [500,200,100,50,20,10,5,2,1]
def WriteProducts():
    for p, q in Products.items():
        print(p, q, "gr")

def EmptyCoins(): # Jeżeli nie ma jakiegoś nominału w automacie to dodaje do listy
    for p in Coins.keys():
        if Coins[p] == 0:
            money.remove(p)

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
highestCoin = max(s for s in Coins.keys() if s < rest if s in money) #znajduje pierwsza najwieksza liczbe mniejsza od reszty
numberOfCoins = Coins[highestCoin] #patrze ile razy moge jej użyć
money.remove(highestCoin) #usuwam ją z listy

if highestCoin*numberOfCoins > rest:
    while highestCoin*numberOfCoins > rest: #zmienjszam jej mnożnik az bedzie mniejsza od reszty
        numberOfCoins -= 1
    solutions = [s for s in change(rest, money, [highestCoin]*numberOfCoins)] #dodaje do poczatkowej listy jej wartość tyle razy ile może sie w niej znaleźć
else:
    solutions = [s for s in change(rest,money,[highestCoin]*numberOfCoins)]

print("Reszta: ",rest," = ",min(solutions,key=len),"gr")

