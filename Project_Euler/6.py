def getSumSquares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

def getSquareSum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum**2


def main():
    sumOfSquares = getSumSquares(100)
    squareSum = getSquareSum(100)
    print('Sum of Squares: {}'.format(sumOfSquares))
    print('Squared Sum: {}'.format(squareSum))
    print('Diff: {}'.format(squareSum-sumOfSquares))

if __name__ == '__main__':
    main()