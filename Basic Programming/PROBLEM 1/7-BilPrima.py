def bilprima(bil) :
    counter = 0
    if bil<2 :
        counter += 1
    else :
        if bil == 2 or bil == 3 :
            counter -= 0
        else :
            for i in range(2, bil-1) :
                if bil % i == 0 :
                    counter += 1
                else :
                    counter += 0

    if counter > 0 :
        return "Bukan Bilangan Prima"
    else :
        return "Bilangan Prima"
        

bil = int(input("Masukan bilangan : "))

print(bilprima(bil))