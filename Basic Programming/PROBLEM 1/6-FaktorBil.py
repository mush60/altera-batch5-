def faktorBil(bil) :
    res = ''
    for i in range(1, bil+1) :
        if bil % i == 0 :
            res = res + str(i)+ ' '
    return res

bil = int(input("Masukan bilangan : "))

print(faktorBil(bil))
# faktorBil(bil)