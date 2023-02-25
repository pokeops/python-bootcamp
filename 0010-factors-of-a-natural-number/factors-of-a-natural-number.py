def main():
    N = int(input())
    for factor in range (1, N+1, 1):
        if N%factor == 0:
                print(factor, end=" ")
    
    return 0

if __name__ == '__main__':
    main()