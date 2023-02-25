def main():
    N = int(input("Enter an integer: "))
    count_f = 0
    if N%2 == 0:
        if N == 2:
            print("YES")
        else:
            print("NO")
    else:
        for factor in range (1, N+1, 1):
            if N%factor == 0:
                count_f = count_f + 1
            if count_f == 2 and factor != N:
                count_f = 3
                break
        if count_f == 2:
            print("YES")
        else:
            print("NO")
if __name__ == '__main__':
    main()