while True:
    try:
        lst = [int(x) for x in input().split()]
        s = sum(lst)
        if s == 3 or s == 0:
            print('*')
        elif s == 2:
            if lst[0] == 0:
                print('A')
            elif lst[1] == 0:
                print('B')
            else:
                print('C')
        else:
            if lst[0] == 1:
                print('A')
            elif lst[1] == 1:
                print('B')
            else:
                print('C')
    except EOFError:
        break