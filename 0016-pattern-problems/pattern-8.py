"""
        1   2   3   4   5   6
        COL COL COL COL COL COL
1   ROW 6   5   4   3   2   1
2   ROW 5   4   3   2   1
3   ROW 4   3   2   1
4   ROW 3   2   1
5   ROW 2   1
6   ROW 1
"""
def main():
    
    N = int(input("Enter the number of rows: "))
    for ROW in range(N, 0, -1):
        for COL in range(ROW, 0, -1):
            print(COL, end=" ")
        print()

    return 0

if __name__ == '__main__':
    main()