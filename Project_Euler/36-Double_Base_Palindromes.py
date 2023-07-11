max_power = 19
powers_2 = [2**n for n in range(max_power, -1, -1)]

def isBinaryPalindrome(num: int) -> bool:
    n = abs(num)
    bin_arr = []
    for i in range(len(powers_2)):
        if powers_2[i] > n and len(bin_arr) == 0:
            pass
        elif powers_2[i] > n and len(bin_arr) > 0:
            bin_arr.append(0)
        else:
            bin_arr.append(1)
            n -= powers_2[i]

    for i in range(len(bin_arr)//2):
        if bin_arr[i] != bin_arr[len(bin_arr)-1-i]:
            # print(bin_arr, 'False')
            return False
    
    # print(bin_arr, 'True')
    return True

def isDecimalPalindrome(num: int) -> bool:
    n = abs(num)
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    #print(digits)
    for i in range(len(digits)//2):
        if digits[i] != digits[len(digits)-1-i]:
            return False
    
    return True


if __name__ == '__main__':
    pal_sum = 0
    for num in range(1, 1000000, 2):
        if isDecimalPalindrome(num) and isBinaryPalindrome(num):
            print(num)
            pal_sum += num
    #print(powers_2)
    print(f'Sum  = {pal_sum}')