"""
        1   2   3   4   5   6
        COL COL COL COL COL COL
1   ROW                     1
2   ROW                 1   2
3   ROW             1   2   3
4   ROW         1   2   3   4
5   ROW     1   2   3   4   5
6   ROW 1   2   3   4   5   6
"""

N = int(input())
for ROW in range(1, N+1, 1):
    SPACES = (N-ROW) * 2
    print(" " * SPACES, end=" ")
    for COL in range(1, ROW+1, 1):
        print(COL, end=" ")
    print()
