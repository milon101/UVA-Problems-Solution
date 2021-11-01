i = 1
while True:
    n = int(input())
    if n==0:
        break
    arr = [int(x) for x in input().split()]
    s = sum(arr)
    d = s / n
    moves = 0
    for b in arr:
        a = b - d
        if a > 0:
            moves += a

    print('Set #{}'.format(i))
    print('The minimum number of moves is {}.'.format(int(moves)))
    print()
    i+=1