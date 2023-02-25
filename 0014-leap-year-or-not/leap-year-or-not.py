def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input("Enter the year: "))
    if A%400==0 or (A%4==0 and A%100!=0):
        print(1)
    else:
        print(0)
    return 0

if __name__ == '__main__':
    main()