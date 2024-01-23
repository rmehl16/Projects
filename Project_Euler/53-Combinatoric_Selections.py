import numpy as np

def calc_factorials(n: int) -> list[int]:
    factorials = [1]
    for i in range(1, n+1):
        factorials.append(int(factorials[i-1] * i))
    return factorials

def calc_combinations(n: int , r:int) -> int:
    # numer_digits = np.arange(1, n+1)
    # denom_digits = np.concatenate([np.arange(1, r+1), np.arange(1, n-r+1)])
    # denom_t1_digits = set(np.arange(1, r+1))
    # denom_t2_digits = set(np.arange(1, n-r+1))

    # print(numer_digits, denom_t1_digits,denom_t2_digits)

    # rmng_numer_digits = []
    # for num in numer_digits:
    #     if num in denom_t1_digits:
    #         denom_t1_digits.remove(num)
    #     elif num in denom_t2_digits:
    #         denom_t2_digits.remove(num)
    #     else:
    #         rmng_numer_digits.append(num)

    # print(rmng_numer_digits, denom_t1_digits, denom_t2_digits)

    upper = max(r, n-r)
    lower = min(r, n-r)
    numer_digits = np.arange(upper+1, n+1)
    denom_digits = np.arange(1, lower+1)

    print(numer_digits, denom_digits)

    print(np.prod(numer_digits) / np.prod(denom_digits))

    print(np.dot(numer_digits, denom_digits))
    

if __name__ == '__main__':
    #print(calc_factorials(10))
    res = calc_combinations(23, 10)