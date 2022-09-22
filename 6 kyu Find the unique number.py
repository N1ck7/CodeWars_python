def find_uniq(arr):
    arr.sort()
    for n in arr:       
        if n != arr[2]:            
            return n
