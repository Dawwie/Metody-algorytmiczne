import math
import numpy as np
import fractions as fra
from pip._vendor.msgpack.fallback import xrange

# Jeżeli wyraz wolny jest zerem
def IfZero(x):
    for item in reversed(x):
        if item == 0:
            x.pop()
        elif item != 0:
            break
    return x

# Dodaje wyrazy przeciwne
def addOpposed(divisors_list):
    empty = []
    for x in divisors_list:
        empty.append(x*-1)
    return empty

# generuje dzielniki danej liczby
def divisorGenerator(n):
    large_divisors = []
    if n < 0:
        n *= -1
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


real = [int(x) for x in input("Liczby rzeczywiste: ").split()] # wejscie
IfZero(real)

l = list(divisorGenerator(int(real[-1])))  # dzielniki wyrazu wolnego
m = list(divisorGenerator(int(real[0])))  # dzielniki wyrazu przy najwyższej potędze

print("Dzielniki wyrazu przy najwyższej potędze ->", list(zip(m, addOpposed(m))))
print("Dzielniki wyrazu wolnego ->", list(zip(l, addOpposed(l))))

empty = []
for i in l:
    empty.append(i * -1)
l.extend(empty)
l.sort()

empty = []
for i in m:
    empty.append(i * -1)
m.extend(empty)
m.sort()

list_of_fractions = []
for i in l:
    for j in m:
         list_of_fractions.append(fra.Fraction(int(i),int(j))) #

no_duplicates = list(set(list_of_fractions))
print("Wszystkie możliwe ułamki ->","; ".join('%s' % item for item in no_duplicates))

list_of_scores = []
print("\nPierwiastek/-ki wielomianu:", end='')
for i in no_duplicates:
    score = np.polyval(real, i)
    if score == 0:
        print("(x - ({}))".format(fra.Fraction(i)), end='')
        list_of_scores.append(i)
print('\n')

# sprawdzanie pierwastków w pochodnych
for i in range (len(list_of_scores)):
    count = 1
    x = list_of_scores.pop()
    for j in range(len(real)):
        derivative = np.polyder(real)
        real = derivative
        if len(derivative) > 0:
            eq_zero = np.polyval(derivative, x)
            if eq_zero == 0:
                count += 1
    print("Pierwiastek {} jest {}-krotny".format(fra.Fraction(x), count))
