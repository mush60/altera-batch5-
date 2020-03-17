def getPrimeNumber(n) :
    count = 0
    for k in range(2, n) :
        if n % k != 0 :
            count += 0
        else :
            count += 1
    return count


def primaSegiEmpat(p, l, x) :
    lprime = p*l
    lsprima = []
    x = x+1
    while len(lsprima) < lprime :
        if x >= 2 : 
            if x == 3 :
                lsprima.append(x)
                x+=1
            else :
                c = getPrimeNumber(x)
                if c > 0 :
                    x += 1
                else :
                    lsprima.append(x)
                    x += 1
        else :
            x+= 1

    ind = 0
    jp = 0
    for i in range(l) :
        for j in range(p) :
            # print(lsprima[index], end = "\t")
            print(lsprima[ind], end="\t")
            jp += lsprima[ind]
            ind += 1
        print()
    print(jp)
    print(lsprima)

vp = int(input("Masukan nilai P : "))
vl = int(input("Masukan nilai L : "))
vx = int(input("Masukan nilai X : "))

primaSegiEmpat(vp, vl, vx)
# hasil = primaSegiEmpat(vp, vl, vx)
# print("Output : {0}".format(hasil))