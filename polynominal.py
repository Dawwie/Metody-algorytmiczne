import math
import numpy as np
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
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

real = [int(x) for x in input("Liczby rzeczywiste: ").split()]

l = list(divisorGenerator(int(real[-1])))# dzielniki wyrazu wolnego
m = list(divisorGenerator(int(real[0]))) # dzielniki wyrazu przy najwyższej potędze

divisors_of_free_word = list(zip(l, addOpposed(l)))
divisors_of_highest_power = list(zip(m, addOpposed(m)))
print("Dzielniki wyrazu przy najwyższej potędze ->",divisors_of_highest_power)
print("Dzielniki wyrazu wolnego ->", divisors_of_free_word)


list_free = l.extend(addOpposed(l))
list_Highest = m.extend(addOpposed(m))