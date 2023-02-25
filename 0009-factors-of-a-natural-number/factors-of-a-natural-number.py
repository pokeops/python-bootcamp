def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    N = int(input("Enter a natural number: "))
    for factor in range (1, N+1, 1):
        if N%factor == 0:
                print(factor, end=" ")
    
    return 0

if __name__ == '__main__':
    main()