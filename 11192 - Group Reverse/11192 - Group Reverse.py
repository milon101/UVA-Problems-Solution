while True:
    inp = input().split()
    n = int(inp[0])
    if n==0:
        break
    arr = inp[1]
    # print(arr)
    out = ''
    start = 0
    # print(len(arr))
    interval =int(len(arr)/n)
    for i in range(n):
        end = start+interval
        out+=arr[start:end][::-1]
        # print(start, end, out)
        start = end
    print(out)
