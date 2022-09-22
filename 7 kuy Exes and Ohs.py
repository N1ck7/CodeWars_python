def xo(s):
    x = 0
    o = 0
    for i in s:
        if i == 'X' or i == 'x':
            x += 1
    for i in s:
        if i == 'O' or i == 'o':
            o += 1
    if x == o:
        return True
    else:
        return False
