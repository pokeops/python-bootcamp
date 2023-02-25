"""
        1   2   3   4   5   6
        COL COL COL COL COL COL
6   ROW 1   2   3   4   5   6
5   ROW 1   2   3   4   5
4   ROW 1   2   3   4   
3   ROW 1   2   3
2   ROW 1   2  
1   ROW 1
"""

def main():

    N = int(input("Enter the number of rows: "))
    for ROW in range(N, 0, -1):
        for COL in range (1, ROW+1, 1):
            print(COL, end=" ")
        print()        #The row has ended. Putting blank print() to move to next line

    return 0

if __name__ == '__main__':
    main()