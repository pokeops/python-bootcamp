def main():
    A = int(input("Enter a positive integer - 'base': "))
    B = int(input("Enter a positive integer - 'exponent' "))
    POW = 1
    for i in range(1, B+1, 1):
        POW = POW * A
    print(POW)

    return 0

if __name__ == '__main__':
    main()