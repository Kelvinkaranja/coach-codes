def reverse(x):
     
    strs = str(x)
    if strs[0] == '-':
            new = "-" + strs[-1:-len(strs):-1]
    else:
            new = strs[-1::-1]

    ma = 2**31-1
    mi = -2**31
    if int(new) < ma and int(new) >mi:
        return int(new)
    else:
        return 0


