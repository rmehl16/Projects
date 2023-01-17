def fib_cap(a=1, b=1, cap=4000000):
    res = a + b
    if res > cap:
        return b
    else:
        return b + fib_cap(b, res) if (b % 2) == 0 else fib_cap(b, res)

# Defining main function
def main():
    print(fib_cap())
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()