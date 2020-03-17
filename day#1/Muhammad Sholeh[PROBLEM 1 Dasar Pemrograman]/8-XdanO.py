def xAndo(xostr) :
    countx = 0
    counto = 0
    for i in xostr :
        if i == 'x' :
            countx += 1
        elif i == 'o' :
            counto += 1
    if(countx == counto) :
        return "True"
    else :
        return "False"

xostr = input("Masukan kata : ")
outp = xAndo(xostr)
print("Output : %s" % (outp))
