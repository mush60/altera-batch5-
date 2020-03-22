def kelompokHewan(list_hewan) :
    init = []
    sorted_init = []
    result = []
    for animal in range(len(list_hewan)) : 
        cdd = list_hewan[animal]
        if cdd[:1] not in init :
            init.append(cdd[:1])
    while len(init) > 0 :
        finit = min(init);
        sorted_init.append(min(init))
        init.remove(finit)
    for j in sorted_init :
        temp = []
        for hwn in list_hewan :
            if j == hwn[:1] :
                temp.append(hwn)
        result.append(temp)
    return result
animals = ['ayam', 'kucing', 'bebek', 'bangau', 'zebra', 'kuda', 'zanggoroo', 'cacing', 'jerapa']

print(kelompokHewan(animals))