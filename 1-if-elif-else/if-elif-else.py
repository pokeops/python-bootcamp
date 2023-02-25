def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input("Enter an integer representing the rating: "))
    if A >= 2100:
        if A%2==0:
            print("GRAND MASTER")
        else:
            print("grand master")
    elif A >= 1900:
        if A%2==0:
            print("CANDIDATE MASTER")
        else:
            print("candidate master")
    elif A >= 1600:
        if A%2==0:
            print("EXPERT")
        else:
            print("expert")
    elif A >= 1400:
        if A%2==0:
            print("PUPIL")
        else:
            print("pupil")
    else:
        if A%2==0:
            print("NEWBIE")
        else:
            print("newbie")

    return 0

if __name__ == '__main__':
    main()