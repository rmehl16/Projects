def getNPrime(num):
    primes = [2]
    curr = 3
    while len(primes) < num:
        is_prime = True
        for prime in primes:
            if curr % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(curr)
        
        curr += 2

    return primes[-1]

if __name__ == '__main__':
    num = 10001
    result = getNPrime(num)
    print(result)