def isPolindrome(s) :
    res = ''
    k = len(s)-1
    while k >= 0 :
        res = res + s[k]
        k -= 1
    
    if res == s :
        return "True"
    else :
        return "False"

mystr = input("Masukan string anda : ")
hasil = isPolindrome(mystr)
print("String %s %s" % (mystr, hasil))

