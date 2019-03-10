Coins = {
        500: 10,
        200: 10,
        100: 10,
        50: 10,
        20: 10,
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
empty = [] #lista na nominały których nie ma w automacie
def WriteProducts():
    for p, q in Products.items():
        print(p, q, "gr")

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
for p in Coins.keys(): # Jeżeli nie ma jakiegoś nominału w automacie to dodaje do listy
    if Coins[p] == 0:
        money.remove(p)

solutions = [s for s in change(rest,money,[])]

print("Reszta: ",rest," = ",min(solutions,key=len),"gr")

