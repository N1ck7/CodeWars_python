def get_day(day, is_leap): 
    
    month = ["January, ","February, ","March, ","April, ","May, ","June, ","July, ","August, ","September, ","October, ","November, ","December, "]
    if is_leap == True:
        if day < 32:
            return month[0] + str(day)
        elif 31 < day < 61:
            return month[1] + str(day - 31)
        elif 60 < day < 92:
            return month[2] + str(day - 60)
        elif 91 < day < 122:
            return month[3] + str(day - 91)
        elif 121 < day < 153:
            return month[4] + str(day - 121)
        elif 152 < day < 183:
            return month[5] + str(day - 152)
        elif 182 < day < 214:
            return month[6] + str(day - 182)
        elif 213 < day < 245:
            return month[7] + str(day - 213)
        elif 244 < day < 275:
            return month[8] + str(day - 244)
        elif 274 < day < 306:
            return month[9] + str(day - 274)
        elif 305 < day < 336:
            return month[10] + str(day - 305)
        elif 335 < day < 367:
            return month[11] + str(day - 335)
    if is_leap == False:
        if day < 32:
            return month[0] + str(day)
        elif 31 < day < 60:
            return month[1] + str(day - 31)
        elif 59 < day < 91:
            return month[2] + str(day - 59)
        elif 90 < day < 121:
            return month[3] + str(day - 90)
        elif 120 < day < 152:
            return month[4] + str(day - 120)
        elif 151 < day < 182:
            return month[5] + str(day - 151)
        elif 181 < day < 213:
            return month[6] + str(day - 181)
        elif 212 < day < 244:
            return month[7] + str(day - 212)
        elif 243 < day < 274:
            return month[8] + str(day - 243)
        elif 273 < day < 305:
            return month[9] + str(day - 273)
        elif 304 < day < 335:
            return month[10] + str(day - 304)
        elif 334 < day < 366:
            return month[11] + str(day - 334)
