test_cases = int(input())
for i in range(test_cases):
    lst = [int(x) for x in input().split()]
    player = lst[1] + lst[2]
    if player <=lst[0]:
        print('Case {}: {}'.format(i+1,player))
    elif player%lst[0] == 0:
        print('Case {}: {}'.format(i+1,lst[0]))
    else:
        print('Case {}: {}'.format(i+1,player%lst[0]))