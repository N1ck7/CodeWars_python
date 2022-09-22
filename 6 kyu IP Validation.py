def is_valid_IP(strng):
    temp=strng.split('.')
    if len(temp)!=4:
        return False
    for str in temp:
        a=0
        if str.isdigit()==False:
            return False
        a=int(str)
        if str[0]=='0' and a!=0:
            return False
        if str == '00':
            return False
        if a<0 or a>255:
            return False
    return True
        
    
        
