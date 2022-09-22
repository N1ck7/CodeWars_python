def disemvowel(string_):
    for i in 'aeuioAEUIO':
        string_ = string_.replace(i,'')
    
    return string_
