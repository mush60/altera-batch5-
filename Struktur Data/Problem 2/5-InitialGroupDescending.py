def initialGrpDesc(names) :
    res = []
    new_names = names.copy()
    sorted_names = []
    for i in range(len(names)) :
        high_name = max(new_names)
        sorted_names.append(high_name)
        new_names.remove(high_name)
    list_init = []
    for i in sorted_names :
        if i[:1] not in list_init :
            list_init.append(i[:1])

    #generate list
    for j in list_init :
        new_list = [j]
        for k in sorted_names :
            if j == k[:1] :
                new_list.append(k)
                
        res.extend([new_list])

    return res


list_name = ['Budi', 'Badu', 'Joni', 'Jono', 'Kaka', 'Doni']

# ls = ['A', 'B', 'C', 'D']

print(initialGrpDesc(list_name))



