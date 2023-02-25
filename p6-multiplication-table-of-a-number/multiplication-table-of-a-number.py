def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input("Enter an integer: "))
    i = 1

    while (i <= 10):
        print(A,"*",i,"=",A*i)
        i = i + 1
    
    return 0

if __name__ == '__main__':
    main()

# One can choose to write the same logic using for loop 
"""
A = int(input())
for i in range (1, 11, 1):
    print(A,"*",i,"=",A*i)
return 0
"""