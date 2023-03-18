def solve(A):
    ans = 0
    i = 1
    while (i * i <= A):
        if A % i == 0:
            if (i == A/i):
                ans = ans + 1
            else:
                ans = ans + 2
        i = i + 1
    return ans

def main():
     n = int(input("Enter a natural number: "))
     print(solve(n))

if __name__ == '__main__':
    main()