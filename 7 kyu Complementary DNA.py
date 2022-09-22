def DNA_strand(dna):
    string = ''
    for i in dna:
        if i == 'A':
            string += 'T'
        if i == 'T':
            string += 'A'
        if i == 'C':
            string += 'G'
        if i == 'G':
            string += 'C'
    return string
