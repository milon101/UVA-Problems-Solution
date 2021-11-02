T = int(input())
for i in range(T):
    N = int(input())
    P = int(input())
    arr = []
    holidays = [6+7*w for w in range(int(N/7)+1)]
    holidays.extend([7+7*w for w in range(int(N/7))])
    # print(holidays)
    for j in range(P):
        h = int(input())
        m = 1
        while (h*m)<=N:
            if h*m not in arr and h*m not in holidays:
                arr.append(h*m)
            m+=1
            
    print(len(arr))