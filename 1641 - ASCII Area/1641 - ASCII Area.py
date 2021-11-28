while True:
    try:
        area = 0
        ind = -1
        flag = False
        poly = ["/", "\\"]
        lst = [int(x) for x in input().split()]
        for i in range(lst[0]):
            ascii = input()
            for j in range(lst[1]):
                if ascii[j] in poly and flag==False:
                    area += .5
                    flag = True
                    ind = j+1
                elif ascii[j] in poly and flag==True:
                    area += (j-ind)+0.5
                    flag = False
        print(int(area))



    except EOFError:
        break