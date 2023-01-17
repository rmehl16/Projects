def isPalindrome(n):
    s = str(n)
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    
    return True


def main():
    max_pal = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if (isPalindrome(int(i*j))) and i*j > max_pal:
                max_pal=i*j

    print(max_pal)
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()