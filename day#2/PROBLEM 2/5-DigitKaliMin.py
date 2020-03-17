def DigitKaliMin(n) : 
    res = 0

    rls = []
    intl = []
    for i in range(1,n+1) :
        if n % i == 0 :
            rls.append(str(i)+""+str(int(n/i)))
    for j in rls :
        intl.append(int(j))

    res += len(str(min(intl)))

    return res

myInt = int(input("Masukan inputan integer : "))
hasil = DigitKaliMin(myInt)
print("Output : {0}".format(hasil))