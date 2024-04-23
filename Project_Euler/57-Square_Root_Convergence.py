
def calcNumDigits(num: int):
    digits = 0
    while abs(num) > 0:
        num = int(num / 10)
        digits += 1
    return digits

def getExpansionsFromPattern(n: int):
    iter_no = 0
    ct = 0
    res = 0
    while ct <= n:
        if (iter_no % 2) == 0:
            ct += 8
        else:
            ct += 5
        res += 1
    return res

if __name__ == '__main__':
    
    count = 0
    expansion = 0

    numerator = 0
    denominator = 1
    for i in range(100):
        numerator += 2*denominator
        
        temp = numerator
        numerator = denominator
        denominator = temp

        expansion += 1

        # print(f'Expansion {expansion}: {numerator + denominator}/{denominator}')

        if calcNumDigits(numerator + denominator) > calcNumDigits(denominator):
            count += 1
            print(f'Expansion {expansion}: {numerator + denominator}/{denominator}')



    num_expansions = getExpansionsFromPattern(1000)
    print(f"Total Num Expansions: {num_expansions}")

