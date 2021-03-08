import copy

while(True):
    N, R, C, K = [int(n) for n in input().split()]

    if (N + R + C + K) == 0:
        break

    lst = []
    lst1 = []
    for i in range(R):
        t = [int(i) for i in input().split()]
        lst.append(t)

    lst1 = copy.deepcopy(lst)

    dir = [[0,1], [1,0], [-1,0], [0,-1]]

    for k in range(K):
        for i in range(R):
            for j in range(C):
                for x in dir:
                    l = i+x[0]
                    m = j+x[1]
                    if l>=0 and m>= 0 and l<R and m < C:
                        if (lst[i][j] - lst[l][m] == -1 or lst[i][j] - lst[l][m] == (N-1)):
                            lst1[l][m] = lst[i][j]
        lst = copy.deepcopy(lst1)
    for x in lst1:
        print(*x)
