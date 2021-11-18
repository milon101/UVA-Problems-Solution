while True:
    try:
        lst = [int(x) for x in input().split()]
        if lst[2] - lst[0] < lst[1]:
            print('Hunters win!')
        else:
            print('Props win!')
    except EOFError:
        break