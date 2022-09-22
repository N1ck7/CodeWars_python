def min_permutation(n):
    min = ''
    ind = 0
    if n >= 0:
        x = [int(a) for a in str(n)]
        x.sort()
        if x[0] == 0 and len(x)>1:
            i = 0
            while x[i] == 0:
                i +=1
            x[0] = x[i]
            x[i] = 0
        for i in x:
            min = min + str(i)
        min = int(min)
        return min
    if n < 0:
        n = n * -1
        x = [int(a) for a in str(n)]
        x.sort()
        
        if x[0] == 0 and len(x)>1:
            i = 0
            while x[i] == 0:
                i +=1
            x[0] = x[i]
            x[i] = 0
        for i in x:
            min = min + str(i)
        min = int(min) * -1
        return min 
