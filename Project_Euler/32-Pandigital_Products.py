import math

def getDigits(num: int):
    num = int(math.fabs(num))
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10
    return digits

def isPandigital(num1: int, num2: int, product: int):
    digits = getDigits(num1) + getDigits(num2) + getDigits(product)
    if len(digits) > 9:
        return None
    elif len(digits) < 9:
        return False
    else:
        digits = set(digits)
        for i in range(1, 10):
            if i not in digits:
                return False
    
    return True

if __name__ == '__main__':
    #print(isPandigital(39,185,39*300))
    pan_dig_products = set()
    for num1 in range(1,10000):
        for num2 in range(1,10000):
            flag = isPandigital(num1, num2, num1*num2)
            
            # Flag that digits 10 or more, so no larger num2 will be processed
            if flag is None:
                break
            
            if flag is True:
                pan_dig_products.add(num1*num2)

    print(pan_dig_products)
    print(sum(pan_dig_products))