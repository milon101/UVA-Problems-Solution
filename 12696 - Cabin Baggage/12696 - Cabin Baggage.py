n = int(input())
allowed_bags = 0
for i in range(n):
    lst = [float(x) for x in input().split()]
    if ((lst[0]<=56.0 and lst[1]<=45.0 and lst[2]<=25.0) or sum(lst[0:3])<=125.0) and lst[3]<=7.0:
        # if lst[3]<=7.0:
        print(1)
        allowed_bags+=1
        # else:
        #     print(0)
    else:
        print(0)
    # print(lst)
print(allowed_bags)