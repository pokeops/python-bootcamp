"""
       1    2   3   4   5   6
       COL COL COL COL COL COL
1   ROW 1
2   ROW 1   2
3   ROW 1   2   3
4   ROW 1   2   3   4
5   ROW 1   2   3   4   5
6   ROW 1   2   3   4   5   6
"""
def main():
    N = int(input("Enter the number of rows: "))
    for ROW in range(1, N+1, 1):
        for COL in range (1, ROW+1, 1):
            print(COL, end=" ")
        print()         #The row has ended. Putting blank print() to move to next line

if __name__ == '__main__':
    main()