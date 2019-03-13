Coins = {
        1000: 1,
        500: 1,
        200: 10,
        100: 0,
        50: 0,
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
    "Orzeszki":170,
    "Baton":140
            }
money = [1000,500,200,100,50,20,10,5,2,1]
def WriteProducts():
    for p, q in Products.items():
        print(p, q, "gr")

def EmptyCoins():
    for p in Coins.keys():
        if Coins[p] == 0:
            money.remove(p)

def RemoveUseless():
    if rest % 5 == 0:
        for i in range(3):
            money.pop()

def beginCoins(allCoins,firstCoin,n):
    count = 1
    if allCoins == firstCoin:
        return 1
    if n - 1 == 0:
        return 0
    for i in range(n):
        if allCoins-firstCoin >= firstCoin:
            count += 1
            allCoins -= firstCoin
        else:
            pass
    return count

def change(n,available_coins,coins_so_far):
    if sum(coins_so_far) == n: #Je?eli sum w li?cie równa sie reszcie do wydania zwraca t? list?
        yield coins_so_far
    elif sum(coins_so_far) > n: #Je?eli sum wi?ksza to nic sie nie dzieje
        pass
    elif available_coins == []: #Je?eli pusta to tez nic
        pass
    else:
        for coin in change(n,available_coins[:],coins_so_far+[available_coins[0]]): #Wywo?uje znów t? funkcj? z tymi samymi monetami i dodaje pierwsza moente do listy
            yield coin
        for coin in change(n,available_coins[1:],coins_so_far):  # tu pobieramy kolejn? monete (inaczej lista sk?ada by sie tylko z tej peirwszej, czyli w naszym przypadku lista by by?a pusta)
            yield coin

customerMoney = input('Podaj sum? pieni?dzy, które chcesz wrzuci?: ')
WriteProducts()
selectProduct = Products.get(input('Wybierz produkt: '))

rest = int(customerMoney) - int(selectProduct)
EmptyCoins()  # Je?eli nie ma jakiego? nomina?u w automacie usuwa z listy
highestCoin = max(
s for s in Coins.keys() if s <= rest if s in money)  # znajduje pierwsza najwieksza liczbe mniejsza od reszty
money.remove(highestCoin)  # usuwam j? z listy
numberOfCoins = Coins[highestCoin]  # ile razy dany nomina? wystepuje w automacie
beginCoins(rest, highestCoin,numberOfCoins)  # funkcja wyliczaj?ca maksymalna liczbe najwiekszych mozliwych nomina?ow które moga byc uzyte do wydania reszty
RemoveUseless()  # usuwa niepotrzebne nomina?y


solutions = [s for s in change(rest, money,[highestCoin]*beginCoins(rest,highestCoin,numberOfCoins))]
print("Reszta: ", rest, " = ", min(solutions, key=len), "gr")
