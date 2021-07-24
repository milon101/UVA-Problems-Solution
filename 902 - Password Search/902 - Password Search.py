from collections import Counter

def substring(str, n):
    sbstr = []
    ln = len(str)
    for i in range(ln):
        if i+n > ln:
            break
        sbstr.append(str[i:i+n])
    return sbstr


while True:
    try:

        line = input().strip()
        while line == "":
            line = input().strip()
    
        line = line.split()
        if len(line) == 2:
            n = int(line[0])
            text = line[1]
        else:
            n = int(line[0])
            text = input().strip()
        while text == "":
            text = input().strip()
        substr = substring(text, n)
        nlist = Counter(substr)
        print(nlist.most_common(1)[0][0])

    except EOFError:
        break

