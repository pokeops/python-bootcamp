def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())                #Input the number of test cases here
    for i in range(1, T+1, 1):         
        N = input()                 #Input the actual number. See typecasting was not done. N= int(input())
        SUM = 0                 
        for i in N:
            SUM = SUM + int(i)
        print(SUM)
    
    return 0

if __name__ == '__main__':
    main()

# This logic used arithmetic operators
""" 
N = int(input())
SUM = 0
while (N>0):
    Q = N // 10  #Floor Operator or Quotient Operator
    R = N % 10   #Modulo Operator    
    SUM = SUM + R
    N = Q
print(SUM)

return 0
"""