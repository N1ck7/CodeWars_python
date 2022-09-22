    def rgb(r, g, b):    
        def OctToHex(num):
            if num <= 0:
                return "00"
            elif num >= 255:
                return "FF"
            mapping = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
            tmp = ""
            while num > 0:
                num, mod = divmod(num, 16)
            
                tmp += mapping[mod]

            return tmp[::-1] if len(tmp) == 2 else "0" + tmp
    
        return OctToHex(r) + OctToHex(g) + OctToHex(b)
