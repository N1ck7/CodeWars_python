def high(x):
    arr,numArr= x.split(' '),[]
    for i in arr:
        intNum = 0
        letters = list(i)
        for word in letters:
            intNum += ord(word) - 96
        numArr.append(intNum)
    return arr[numArr.index(max(numArr))]
