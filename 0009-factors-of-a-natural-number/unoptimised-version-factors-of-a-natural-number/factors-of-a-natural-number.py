def solve(N):
    ans = 0
    for i in range (1, N+1, 1):
        if N % i == 0:
                ans = ans + 1
    return ans

def main():
     n = int(input("Enter a natural number: "))
     print(solve(n))

if __name__ == '__main__':
    main()