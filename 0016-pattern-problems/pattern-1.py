"""
       1    2   3   4   5   6
       COL COL COL COL COL COL
1   ROW *
2   ROW *   *
3   ROW *   *   *
4   ROW *   *   *   *
5   ROW *   *   *   *   *
6   ROW *   *   *   *   *   *
"""

def main():
    N = int(input("Enter the number of rows: "))
    for ROW in range(1, N+1, 1):
        print("* " * ROW)
    
    return 0

if __name__ == '__main__':
    main()