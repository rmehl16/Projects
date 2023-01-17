import numpy as np

# def getPrimesThroughN(n):
#     primes = [2]
#     for i in range(3, n):
#         is_prime = True
#         for prime in primes:
#             if i % prime == 0:
#                 is_prime = False
#                 break
        
#         if is_prime:
#             primes.append(curr)
        
#     return primes


def getTriangleSum(n):
    return int(np.sum(np.arange(n+1)))

def getDivisors(n, cut=1):
    num_div = 0
    for i in range(1, cut):
        if n % i == 0:
            num_div += 1

    if n % 2 == 1:
        for i in range(1, int(n/cut)+1, 2):
            if n % i == 0:
                num_div += 1
    else:
        for i in range(1, int(n/cut)+1):
            if n % i == 0:
                num_div += 1

    #print(n, res)
    return num_div

if __name__ == '__main__':
    min_divisors = 500

    divisors = 0
    triangle = 1000
    tri_sum = getTriangleSum(triangle)
    i = 0
    while divisors < min_divisors:
        tri_sum = getTriangleSum(triangle)
        divisors = getDivisors(tri_sum, cut=500)
        if divisors > 250:
            print(triangle, tri_sum, divisors)
        triangle += 1


    print(tri_sum, divisors)
