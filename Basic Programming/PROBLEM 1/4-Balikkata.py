def revkata(kata) :
    res = ''
    k = len(kata)-1
    while k >= 0 :
        res = res + kata[k]
        k -= 1

    return res

kata = input("Masukan Kata untuk di balik : ")
print(revkata(kata))
