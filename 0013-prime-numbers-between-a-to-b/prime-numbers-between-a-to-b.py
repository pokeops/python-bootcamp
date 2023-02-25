def main():
    A = int(input("Enter the first number: "))
    B = int(input("Enter the second number: "))
    if A >= B:              #This logic has been put to that code works from (0-100)             
        MAX = A             # and (100-0) as well
        MIN = B
    else:
        MIN = A
        MAX = B
    for N in range(MIN, MAX+1, 1):
        if N % 2 == 0:
            if N == 2:      # No even number is prime, except 2
                print(N, end=" ")
        else: 
            count_f = 0
            for factor in range(1, N+1, 1):
                if N % factor == 0:
                    count_f += 1
                if count_f == 2 and factor != N:
                    count_f = 3
            if count_f == 2:
                print(N, end=" ")

    return 0

if __name__ == '__main__':
    main()