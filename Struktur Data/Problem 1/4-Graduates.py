def Gradueate(ldict) :
    resDisct = {}
    listClass = []
    for d in ldict :
        if d["class"] not in listClass :
            listClass.append(d["class"])
    if len(ldict) > 0 :
        resDisct = {'Foxes' : {}, 'Wolfes' : {}, 'Tigers' : {}}
        
        for i in range(len(listClass)) :
            temp = []
            for j in ldict :
                if j["class"] == listClass[i] and j["score"] > 75:
                    temp.append({"name" : j["name"], "score" : j["score"]})
            resDisct[listClass[i]] = temp
        return resDisct
    else :
        return resDisct  




siswa = [
    {'name' : 'Ardi', 'score' : 91, 'class' : 'Tigers'},
    {'name' : 'Sholeh', 'score' : 90, 'class' : 'Wolfes'},
    {'name' : 'Yopi', 'score' : 80, 'class' : 'Foxes'},
    {'name' : 'Alul', 'score' : 70, 'class' : 'Wolfes'},
    {'name' : 'Andre', 'score' : 94, 'class' : 'Tigers'},
    {'name' : 'Bagas', 'score' : 90, 'class' : 'Wolves'},
    {'name' : 'Rizal', 'score' : 89, 'class' : 'Foxes'}
]

siswa2 = [
    {
        'name' : 'John',
        'score' : 64,
        'class' : 'Foxes'
    },    
    {
        'name' : 'Jene',
        'score' : 90,
        'class' : 'Tigers'
    },
    {
        'name' : 'Doe',
        'score' : 60,
        'class' : 'Tigers'
    },
]

print(Gradueate(siswa))
print("======")
print(Gradueate(siswa2))
print("======")
print(Gradueate([]))
