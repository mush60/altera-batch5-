def bilanganUnik(number):
    list_unik = []
    for i in range(2, number+1) :
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 :
            continue
        else :
            list_unik.append(i)

    res = ''
    for j in range(len(list_unik)) :
        res = res + str(list_unik[j]) + " "
    print(res)

bilanganUnik(20)
