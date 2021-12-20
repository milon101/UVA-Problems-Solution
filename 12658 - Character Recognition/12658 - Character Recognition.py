n = int(input())

lst = []
for i in range(5):
    lst.append(input().split())

# print(lst)
digits = ''
s = lst[3][0]
for i in range(0, n*4, 4):
    # print(s)
    if   s[i]  == '*':
        digits +='2'
    elif s[i+1]=='*':
        digits +='1'
    elif s[i+2]=='*':
        digits +='3'
print(digits)