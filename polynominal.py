import math
import string as s
import numpy as np
import fractions as fra
from pip._vendor.msgpack.fallback import xrange


def poly(divisors_list,real_numbers):
    np.polyval()

def addOpposed(divisors_list):
    empty = []
    for x in divisors_list:
        empty.append(x*-1)
    return empty

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

real = [int(x) for x in input("Liczby rzeczywiste: ").split()]
l = list(divisorGenerator(int(real[-1])))  # dzielniki wyrazu wolnego
m = list(divisorGenerator(int(real[0])))  # dzielniki wyrazu przy najwyższej potędze

divisors_of_highest_power = list(zip(m, addOpposed(m)))
divisors_of_free_word = list(zip(l, addOpposed(l)))
print("Dzielniki wyrazu przy najwyższej potędze ->", divisors_of_highest_power)
print("Dzielniki wyrazu wolnego ->", divisors_of_free_word)

empty = []
for i in l:
    empty.append(i * -1)
l.extend(empty)
l.sort()
#print(l)

empty = []
for i in m:
    empty.append(i * -1)
m.extend(empty)
m.sort()
#print(m)

list_of_fractions = []
for i in l:
    for j in m:
        x = i/j
        list_of_fractions.append(round(x,1))

no_duplicates = list(set(list_of_fractions))
print("Wszystkie możliwe ułamki ->",no_duplicates)

list_of_scores = []
print("\nPierwiastek/-ki wielomianu:",end='')
for i in no_duplicates:
    score = np.polyval(real, i)
    if score == 0:
        print("(x - (%s))" % fra.Fraction(i),end='')
        list_of_scores.append(i)
    elif score != 0 and score in list_of_scores:
        print("\nPierwiastek %s jest pierwiastkiem %s krotnym " % (fra.Fraction(i), no_duplicates.count(i)+1))
print(list_of_scores)
#dodac sprawdzanie krotnosci pierwiastka
