while True:
    try:
        tea_type = input()
        lst = input().split()
        print(lst.count(tea_type))
    except EOFError:
        break