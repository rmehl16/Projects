import math

def getPowerDigitSum(base, exp):
    num = base**exp
    digit_sum = 0
    while num != 0:
        print(num, digit_sum)
        digit_sum += num % 10
        num = num // 10

    return digit_sum

if __name__ == '__main__':
    base = 2
    exp = 1000
    res = getPowerDigitSum(base, exp)
    print(res)
