def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input("Enter 1st natural number: "))
    B = int(input("Enter 2nd natural number: "))
    if A <= B:          #Optimization is happening here
        MIN = A
    else:
        MIN = B    
    for factor in range (1, MIN+1, 1):
        if A%factor == 0 and B%factor == 0:
            print(factor, end=" ")

    return 0
    
if __name__ == '__main__':
    main()