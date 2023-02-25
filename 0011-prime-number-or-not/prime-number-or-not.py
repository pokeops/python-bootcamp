def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    N = int(input("Enter a natural number: "))
    if N == 1:
        print(N,"is neither prime nor composite")
    elif N % 2 == 0:
        if N == 2:
            print("YES")
        else:
            print("NO")
    else:
        count_f = 0
        for factor in range(1, N+1, 1):
            if N % factor == 0:
                count_f += 1
            if count_f == 2 and factor != N:
                count_f = 3
        if count_f == 2:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()