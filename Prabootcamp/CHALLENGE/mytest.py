myint = int(input("masukan integer : "))

def revint(myint) :
    if myint in range(-2**31, 2**31-1) :
        res = ''
        nstr = str(abs(myint))
        res = res + nstr[::-1]
        
        res = int(res)

        if myint < 0 :
            return -res
        else :
            return res
    else :
        return 0

print(revint(myint))