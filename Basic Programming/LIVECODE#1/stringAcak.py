def stringAcak(stringSatu, stringDua):
    list_s1 = []
    list_s2 = []
    list_count = []
    for i in stringSatu :
        list_s1.append(i)
    for j in stringDua :
        list_s2.append(j)

    for k in range(len(list_s1)) :
    	count = 0
    	if list_s1[k] in list_s2 :
    		idx = list_s2.index(list_s1[k])
    		list_s2.pop(idx)
    	list_count.append(count)

    print(list_count)
    print(list_s1)
    print(list_s2)

def stringAcak2(stringSatu, stringDua) :
    for i in stringSatu :
        newstr = stringDua.replace(i,'')

    print(newstr)

stringAcak2("alterra", "terlata")