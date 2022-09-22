def get_count(sentence):
    x = 0
    for i in sentence:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            x = x+1
    return x           
