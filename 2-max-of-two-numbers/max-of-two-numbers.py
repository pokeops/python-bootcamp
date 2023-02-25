def main():
    A = int(input("Enter first integer: "))
    B = int(input("Enter second integer: "))
    if A >= B:          #If A is bigger than B
        print(A)
    else:              #If B is bigger than A
        print(B)
    return 0

if __name__ == '__main__':
    main()