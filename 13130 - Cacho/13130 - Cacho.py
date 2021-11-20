T = int(input())
for i in range(T):
    lst = [int(x) for x in input().split()]
    flag = True
    for i in range(1, 5):
        if lst[i]-lst[i-1] != 1:
            flag = False
            break
    if flag:
        print('Y')
    else:
        print('N')

