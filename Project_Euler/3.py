# def getPrimeFactors(n, q=[]):
#     factors =set()
#     for i in range(2, int(n/2)+1):
#         if (n % i) == 0:
#             factors.add(i)

#     if len(factors) == 0:
#         return [n]
    
#     primes = set()
#     for factor in factors:
#         if factor in primes:
#             continue
#         x = getPrimeFactors(factor)
#         for a in x:
#             primes.add(a)

#     return primes


def getFactors(n):
    factors = []
    for i in range(2, int(n/2)+1):
        if (n % i) == 0:
            factors.append(i)

    return factors

def isPrime(n):
    for i in range(2, int(n/2)+1):
        if (n % i) == 0:
            return False
    return True

def getLargestFactor(n):
    for i in range(2, int(n/2)+1):
        if (n % i) == 0:
            print(i)
            return getLargestFactor(int(n / i))
    return n

def main():
#    result = getPrimeFactors(600851475143)
    #result = getFactors(600851475143)
    #result.reverse()
    #for factor in result:
    #     if isPrime(factor):
    #         print(factor)
    result = getLargestFactor(600851475143)
    print(result)
    
# Using the special variable 
# __name__
if __name__=="__main__":
    main()