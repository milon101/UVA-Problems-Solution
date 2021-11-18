n = int(input())

for i in range(n):
    lst = [int(x) for x in input().split()]
    if lst.count(0)==0:
        print('Set #{}: Yes'.format(i+1))
    else:
        print('Set #{}: No'.format(i+1))