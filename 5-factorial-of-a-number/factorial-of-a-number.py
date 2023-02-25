def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input("Enter a positive integer here: "))
    FACT = 1
    for i in range(1, N+1, 1):
        FACT = FACT * i
    print(str(N) + "!" + " is equal to", FACT)

if __name__ == '__main__':
    main()


# One can choose to write the same logic using while loop 
"""
N = int(input("Enter a positive integer here: "))
FACT = 1
i = 1
while i <= N:
    FACT = FACT * i
    i += 1
print(str(N) + "!" + " is equal to", FACT)
"""