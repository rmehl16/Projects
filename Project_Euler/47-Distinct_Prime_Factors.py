primes = []

'''
Calculate primes in range (2,n] and populate global variable
'''
def calculatePrimes(n: int):
    if n < 2:
        print('Pass in positive integer >= 2')
        return
    
    primes.append(2)
    for num in range(3, n+1, 2):
        isPrime = False
        for prime in primes:
            if (num % prime) == 0:
                break
            elif prime > int(num/2):
                isPrime = True
                break
        if isPrime:
            primes.append(num)

def getDistinctPrimeFactors(n: int) -> list:
    prime_factors = []
    for prime in primes:
        if (n % prime) == 0:
            prime_factors.append(prime)
    return prime_factors

if __name__ == '__main__':
    
    # Calculate primes
    calculatePrimes(1000)
    # print(primes)

    tgt_nums = []
    tgt_streak = 4
    for i in range(1, 1000000):
        f = getDistinctPrimeFactors(i)
        if len(f) == 4:
            tgt_nums.append(i)
            if len(tgt_nums) == tgt_streak:
                print(tgt_nums)
                break
        else:
            tgt_nums = []




