T = int(input())
for i in range(T):
    n = int(input())
    y = 0
    flag = False
    for j in range(n):
        result = input()
        if result=='L' or result=='D':
            y+=1
        else:
            y=0
        if y==3 and not flag:
            print('Case {}: {}'.format(i+1, j+1))
            flag=True
            continue
    if y<3 and not flag:
        print('Case {}: Yay! Mighty Rafa persists!'.format(i+1))