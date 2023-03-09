def nCr(a,b):               #nCr= n! / (r! * n-r!)
    NUM = FACT(a)
    DEN = FACT(b) * FACT(a-b)
    return int(NUM/DEN)      
#   return NUM//DEN         (You can return NUM // DEN as well.)

def FACT(x):
    F = 1
    for i in range(1, x+1, 1):
        F = F * i
    return F

def main():
    n = int(input("Enter value of n: "))
    r = int(input("Enter value of r: "))
    print(nCr(n,r))

    return 0

if __name__ == '__main__':
    main()