def MY_CEIL(x):
    if x >= 0:
        if x == int(x):
            print(int(x))
        else:
            print(int(x+1))
    else:
            print(int(x))

def main():
    MY_CEIL(-2.2)
    MY_CEIL(2)
    MY_CEIL(3.2)
    MY_CEIL(-4.9)


if __name__ == '__main__':
    main()