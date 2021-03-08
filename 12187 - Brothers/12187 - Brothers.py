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

    
    for k in range(K): 

        for i in range(R):
            for j in range(C-1):
                if (lst[i][j] - lst[i][j+1]) == -1 or (lst[i][j] - lst[i][j+1]) == (N-1):
                    lst1[i][j+1] = lst[i][j]
                    
                if (lst[i][j] - lst[i][j+1]) == 1 or (lst[i][j] - lst[i][j+1]) == -(N-1):
                    lst1[i][j] = lst[i][j+1]

        for i in range(C):
            for j in range(R-1):
                
                if (lst[j][i] - lst[j+1][i]) == 1 or (lst[j][i] - lst[j+1][i]) == -(N-1):
                    lst1[j][i] = lst[j+1][i]

                if (lst[j][i] - lst[j+1][i])== -1 or (lst[j][i] - lst[j+1][i])== (N-1):
                    lst1[j+1][i] = lst[j][i]
        lst = copy.deepcopy(lst1)
    for x in lst1:
        print(*x)
