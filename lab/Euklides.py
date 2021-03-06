import random
import time
import math


def is_prime(num):
    for j in range(2, int(math.sqrt(num)) + 1):
        if (num % j) == 0:
            return False
    return True

# a = int(raw_input('a = '))
# b = int(raw_input('b = '))
#
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# else:
#     print 'gcd = ', a


def euklides(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

# print euklides(160, 120)


def euklides2(*args):
    return reduce(euklides, args)

lista = [16, 4, 8]
print euklides2(9, 6, 12, 99, 30)

# print reduce(lambda x,y: x+y,[1,2,3])

# print map(lambda x: x+1, [1])

big1 = random.getrandbits(256)
big2 = random.getrandbits(256)
fst = 1000000000L
snd = 1000010000L
big3 = filter(is_prime, range(fst, snd))
print len(big3)

prime = 0
if big3:
    prime = big3[0]
else:
    prime = 997
print big1, big2, prime

start = time.time()
print euklides(prime * prime, prime * prime * prime)
stop = time.time()
print 'Time:', stop - start
