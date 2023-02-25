def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    A = int(input("Enter first integer: "))
    B = int(input("Enter second integer: "))
    if A >= B:          #If A is bigger than B
        print(A)
    else:              #If B is bigger than A
        print(B)
    return 0

if __name__ == '__main__':
    main()