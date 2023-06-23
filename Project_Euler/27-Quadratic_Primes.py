import math


def isPrime(num):
    if num in primes:
        return True
    elif (num % 2) == 0:
        return False
    elif num == 1:
        return True
    
    for i in range(3, int(math.fabs(num)), 2):
        if (num % i) == 0:
            return False

    primes.add(num)
    return num

if __name__ == '__main__':
    global primes 
    primes = set()

    a_lim = 1000
    b_lim = 1000

    ab_n_map = dict()
    for a in range(-1*a_lim + 1, a_lim):
        for b in range(-1*b_lim, b_lim+1):
            n = 0
            while True:
                q = n**2 + (a*n) + b
                if not isPrime(q):
                    if ab_n_map.get((a,b), 0) != 0:
                        ab_n_map[(a,b)] = max(n, ab_n_map[(a,b)])
                    else:
                        ab_n_map[(a,b)] = n
                    break
                n +=1

    #print(sorted(list(primes)))

    #max_keys = [(key,value) for key, value in ab_n_map.items() if value == max(ab_n_map.values())]
    max_val = max(ab_n_map.values())
    print(max_val)
    for k,v in ab_n_map.items():
        if v == max_val:
            print(k, k[0]*k[1])
    
