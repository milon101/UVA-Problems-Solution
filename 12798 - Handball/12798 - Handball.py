while True:
    try:
        NM = [int(x) for x in input().split()]
        players = 0
        for i in range(NM[0]):
            lst = [int(x) for x in input().split()]  
            if not any(t==0 for t in lst):
                players+=1
        print(players)

    except EOFError:
        break