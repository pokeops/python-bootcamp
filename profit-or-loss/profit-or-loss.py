def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    C = int(input())    #Enter the cost price
    S = int(input())    #Enter the selling price
    if S > C:           #If S.P > C.P, you will make profits
        print(1)
        print(S-C)      #Profit = S.P. - C.P.
    else:               #Else, you will make a loss
        print(-1)
        print(C-S)      #Loss = C.P. - S.P.
    return 0

if __name__ == '__main__':
    main()