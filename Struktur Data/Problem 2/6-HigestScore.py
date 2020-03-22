def higestScore(students) :
    classes = []
    for i in students :
        if i['class'] not in classes :
            classes.append(i['class'])

    res = {}
    for kelas in classes :
        subres = {}
        for student in students :
            if student['class'] == kelas :
                if len(subres) == 0 :
                    subres = {'name' : student['name'], 'score' : student['score']}
                else : 
                    if subres['score'] < student['score']  :
                        subres = {'name' : student['name'], 'score' : student['score']}
        
        res[kelas] = subres
    # for i in range(len(students)-1) :
    #     for j in range(len(students)) :
    #         if students[i]['score'] > students[j]['score'] :
    #             temp = students[i]
    #             students[i] = students[j]
    #             students[j] = temp

    return res

print(higestScore([{'name' : 'Dimitri', 'score' : 90, 'class' : 'foxes'},
    {'name' : 'Alexi','score' : 85,'class' : 'wolves'},
    {'name' : 'Sigrei','score' : 100,'class' : 'foxes'},
    {'name' : 'Dimitri','score' : 90,'class' : 'foxes'},
    {'name' : 'Anatasia','score' : 78,'class' : 'wolves'},
    {'name' : 'Derbi','score' : 99,'class' : 'tigers'},
    {'name' : 'Yogie','score' : 78,'class' : 'snakes'}]))


    # ,
    # {
    #     'name' : 'Anatasia',
    #     'score' : 78,
    #     'class' : 'wolves'
    # },
    # {
    #     'name' : 'Anatasia',
    #     'score' : 78,
    #     'class' : 'wolves'
    # },
    # {
    #     'name' : 'Anatasia',
    #     'score' : 78,
    #     'class' : 'wolves'
    # }
