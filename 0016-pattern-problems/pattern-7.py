"""
        1   2   3   4   5   6
        COL COL COL COL COL COL
6   ROW          1
5   ROW        1   2
4   ROW      1   2   3
3   ROW    1   2   3   4
2   ROW   1   2   3   4   5
1   ROW 1   2   3   4   5   6
"""
def main():
    N = int(input("Enter the number of rows: "))
    for ROW in range(1, N+1, 1):
        print ((N-ROW) * " ", end=" ") 
        for COL in range (1, ROW+1, 1):
            print(COL, end=" ")
        print()
    
    return 0

if __name__ == '__main__':
    main()