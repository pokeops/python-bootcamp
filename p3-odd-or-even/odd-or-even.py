def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input("Enter an integer: "))
    if N % 2 == 0:
        print(0)     #print 0 if it is even
    else:
        print(1)     #Print 1 if it is odd
    return 0

if __name__ == '__main__':
    main()