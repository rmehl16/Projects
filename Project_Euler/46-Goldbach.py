def calc_squares_x_2(n: int) -> list:
    res = set()
    for i in range(1, n+1):
        res.add(int(2 * i**2))
    return res

def isPrime(n: int) -> bool:
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n/2), 2):
        if (n % i) == 0:
            return False
        
    return True



if __name__ == '__main__':
    squares = calc_squares_x_2(250)

    primes = [2]

    cur = 1
    while cur < 100000:
        cur += 2
        if isPrime(cur):
            primes.append(cur)
        else:
            has_solution = False
            for prime in primes:
                val = cur - prime
                if val in squares:
                    # print(prime, val, cur)
                    has_solution=True
                    break
            if not has_solution:
                print(prime, val, cur)
                break
                

    # print(primes)
