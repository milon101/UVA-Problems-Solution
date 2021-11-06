while True:
    t = [int(x) for x in input().split(':')]
    if sum(t) == 0:
        break
    # print(t)
    angle = abs(((t[0])*30 + (t[1]*.5)) - ((t[1])*6))
    if angle >180:
        angle = 360 - angle
    print('{:.03f}'.format(angle))