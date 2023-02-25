def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    month = input("Enter the month of the year: ")
    match month:
        case "January" | "March" | "May" | "July" | "August" | "October" | "December":
            print(31)
        case "April" | "June" | "September" | "November":
            print(30)
        case _:
            print(28)

    return 0

if __name__ == '__main__':
    main()