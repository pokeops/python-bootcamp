def FACT(n):
    F = 1
    for i in range(1, n+1, 1):
        F = F * i
    return F

def main():
    N = int(input("Enter the number: "))
    print("Factorial of", N, "is", FACT(N))

if __name__=='__main__':
    main()