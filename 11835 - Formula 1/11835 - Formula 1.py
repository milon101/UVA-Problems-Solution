from collections import defaultdict
while True:
    d = defaultdict(int)
    gp = [int(x) for x in input().split()]
    if sum(gp) == 0:
        break
    result = []
    for i in range(gp[0]):
        result.append([int(x) for x in input().split()])
    # print(gp, result)
    # print(d)
    S = int(input())
    for i in range(S):
        for g in range(gp[1]):
            d[g] = 0
        arr = [int(x) for x in input().split()]
        # print(arr)
        # print(d)
        for j in range(gp[0]):
            for p in range(gp[1]):
                t = result[j][p]
                if arr[0] >= t:
                    # print(t)
                    d[p] += arr[t]
    
        # print(d)
        max_value = max(d.values())
        max_keys = [k+1 for k,v in d.items() if v == max_value]
        print(*max_keys)
