def unique_in_order(iterable):
    try:
        order = []
        x = 0
        if iterable == '':
            return order

        order += iterable[0]
        for i in iterable:
            if i!= order[-1]:
                order += i
                x += 1         
        return order
    except:
        n = []
    for i in iterable:
        if i not in n:
            n.append(i)
    return n
    
    
