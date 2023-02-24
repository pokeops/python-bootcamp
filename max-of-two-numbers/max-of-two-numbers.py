def main():
    A = int(input("Enter first integer: "))
    B = int(input("Enter second integer: "))
    if (A>B):          #If A is bigger than B
        print(A, "is the maximum among the 2 numbers")
    else:              #If B is bigger than A
        print(B, "is the maximum among the 2 numbers")
    return 0

if __name__ == '__main__':
    main()