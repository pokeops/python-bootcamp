"""
        1   2   3   4   5   6
        COL COL COL COL COL COL
1   ROW                     6  
2   ROW                 6   5
3   ROW             6   5   4
4   ROW         6   5   4   3
5   ROW     6   5   4   3   2
6   ROW 6   5   4   3   2   1
"""

def main():
        N = int(input("Enter the number of rows: "))
        for ROW in range(1, N+1, 1):
                SPACES = (N-ROW) * 2
                print(" " * SPACES, end="")
                for COL in range(1, ROW+1, 1):
                       print(N-COL+1, end=" ")
                print()
        return 0
    
if __name__ == '__main__':
    main()