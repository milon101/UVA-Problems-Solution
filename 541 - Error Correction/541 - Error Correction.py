while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    # flag = 0
    for i in range(n):
        tmp = [int(j) for j in input().split()]
        arr.append(tmp)
        # if sum(tmp) % 2 != 0:
        #     flag = 1
        # if i == (n-1):
    row = []
    col = []
    arr_col = [sum(x) for x in zip(*arr)]
    for i in range(n):
        if sum(arr[i]) %2 != 0:
            row.append(i+1)
        if arr_col[i] %2 != 0:
            col.append(i+1)
    # print(arr)
    # print(row, col)
    if not row and not col:
        print('OK')
    elif len(row)==1 and len(col)==1:
        print('Change bit ({},{})'.format(row[0], col[0]))
    else:
        print('Corrupt')
