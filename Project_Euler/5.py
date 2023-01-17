def isDivisible(n):
    for i in range(1,21):
        if n % i != 0:
            return False
    return True

def getSmallestMultiple():
    n = int(19*20)
    while True:
        if isDivisible(n):
            return n
        else:
            n += int(19*20)
            if n > 232792560:
                print('x')
                return 0



def main():
    print(getSmallestMultiple())
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()