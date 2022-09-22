def to_nato(words):
    dictionary = {'A':'Alfa', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H':'Hotel', 'I':'India', 'J':'Juliett', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
    words = words.upper()
    words = words.replace(' ', '')
    nato = ''
    for i in words:
        if i == '.' or i == '!' or i == '?':
            nato += i
            nato += ' '
        else:
            nato = nato + dictionary[i]
            nato += ' '
    return nato.rstrip()
