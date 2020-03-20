def listToDict(lists) :
    resDict = {}
    res = ['firstName', 'lastName', 'gender', 'age']
    for i in range(len(lists)) :
        subDict = {}
        title = str(i+1)+' '+ lists[i][0] + ' ' + lists[i][1]
        
        for j in range(len(res)) :
            if len(lists[i]) != len(res) :
                lists[i].append('Invalid')
            if isinstance(lists[i][3], int) == True :
                if lists[i][3] < 2020 :
                    lists[i][3] = 2020 - lists[i][3]
                else :
                    lists[i][3] = 'Invalid'

            subDict[res[j]] = lists[i][j]

        resDict[title] = subDict

    return resDict

print(listToDict([['Christ', 'Evans', 'Male', 1982], ['Robert', 'Downey', 'Male']]))
print(listToDict([['Christ', 'Evans', 'Male', 1982], ['Robert', 'Downey', 'Male'], ['Muhammad', 'Sholeh', 'Male', 2021]]))