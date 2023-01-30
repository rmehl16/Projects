# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n)
def construct_d_func(n: int) -> list:
    d = [0]
    for i in range(1, n):
        div_sum = 0
        for j in range(1, max(2, (i//2)+1)):
            #print(i, j)
            if i % j == 0:
                div_sum += j
        d.append(div_sum)
    #print(d)
    return d

def findAmicableNums(l: list) -> set:
    amicables = set()
    for i in range(len(l)):
        if l[i] < len(l) and i == l[l[i]] and i != l[i]:
            amicables.add(i)
            amicables.add(l[i])
            print(i, l[i])

    return amicables

if __name__ == '__main__':
    N = 10000
    d_n = construct_d_func(N)
    amic_nums = findAmicableNums(d_n)
    print(f'The sum of amicable numbers is {sum(amic_nums)}')
