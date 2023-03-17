def MY_RANGE(start, stop, step=1):
    if step > 0:
        x = start
        while x < stop:
            if x == stop-step:
                print(x, end= "")
            else:
                print(x, end= ",")
            x = x + step
        print()
    else:
        x = start
        while x > stop:
            if x == stop-step:
                print(x, end= "")              
            else:
                print(x, end= ",")
            x = x + step
        print()

    return None

def main():
    MY_RANGE(10,6,-1)
    MY_RANGE(6,10,1)
    MY_RANGE(6,20,2)
    MY_RANGE(-6,-16,-2)

    return None

if __name__ == '__main__':
    main()