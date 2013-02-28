# -*- coding:utf8 -*-
import random
import math
import time

# generate a random Prime with length 'L'
def gen_rand(L):
    n = random.getrandbits(L)
    n = bin(n)[2:]
    bits = len(n)
    n = '0'*(L-bits) + n
    # n now is a str length L , made of '0'/'1'    
    # set low bit and 2 highest bits to '1'
    n = '11' + n[2:L-1] + '1'

    # return an Int
    return int(n, 2)

def pow_and_mod(a, q, n):
    # calc a ** q % n in a quick way
    res = 1
    while q > 0:
        if q % 2:
            res = res * a % n
        a = a * a % n
        q >>= 1
    return res

def Miller_Rabin(n):
    # test if n is a prime.
    n_1 = n-1
    q = n_1
    k = 0
    while q % 2 == 0:
        q /= 2
        k += 1
    a = random.randrange(2,n_1)
    if a * q % n == 1:
        return True
    #t = a ** q % n
    t = pow_and_mod(a, q, n)
    for  j in range(k):
        if  t in (1, n_1):
            return True
        else:
            t = t * t % n
    return False
    
def is_Prime(n):
    for i in range(5):
        if not Miller_Rabin(n):
            return False
    return True

def gen_rand_prime(L):
    n = gen_rand(L)
    while True:
        if is_Prime(n):
            return n
        else:
            n += 2
    return n

def gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp
    if b == 0:
        return a
    return gcd(b, a % b)

"""
while True:
    x = int(raw_input('x:'))
    y = int(raw_input('y:'))
    print gcd(x, y)
"""

def Ex_Euclid(m, b):
    (a1, a2, a3) = (1, 0, m)
    (b1, b2, b3) = (0, 1, b)
    while True:
        if b3 == 0:
            #a3 = gcd(m, b)
            return a3
        if b3 == 1:
            #b3 = gcd(m, b)
            return b2
        q = a3 / b3
        
        (t1, t2, t3) = (a1 - q * b1, a2 - q * b2, a3 - q * b3)
        (a1, a2, a3) = (b1, b2, b3)
        (b1, b2, b3) = (t1, t2, t3)
        #print (q, a1, a2, a3, b1, b2, b3)

def RSA_generate_key(L):
    # generate a L-length Key. ( p, q, n, e, d)
    while True:
        p = gen_rand_prime(L/2)
        q = gen_rand_prime(L-L/2)
        n = p * q
        fi = (p - 1) * (q - 1)
        e = 65537
        d = Ex_Euclid(fi, e)
        if d > 0:
            break
    # Public Key -- (e, n)
    # Private Key - (d, n)
    return (p, q, n, e, d)

"""
Unit Test -- gen_rand_prime
for L in range(1024, 1025, 10):    
    t = time.time()
    print L, gen_rand_prime(L)
    tt = time.time()
    print 'Total time:', tt-t
"""
