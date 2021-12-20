T  = int(input())

for i in range(T):
        n = int(input())
        max_value = int(input())
        max_score = -1500000
        flag = False
        for i in range(n-1):
            c = int(input())
            if max_score < (max_value - c):
                max_score = max_value - c
            if max_value < c:
                max_value = c
        print(max_score)

        # n = int(input())
        # lst = [int(input())]
        # max_score = -1500000000
        # for i in range(n-1):
        #     c = int(input())
        #     for x in lst:
        #         if (x - c) > max_score:
        #             max_score = x - c
        #     lst.append(c)
        # print(max_score)
