ls = [3, 1, 5, 5, 5, 2, 5, 2, 6, 87, 52]
search_dict = [{"nama" : "aji"}, {"nama" : "shofi"}]

def search(ls) :
    for i in range(len(ls)) :
        if ls[i] == 2 :
            return i

def searchObj(tdict, target) :
    for i in tdict :
        if i["nama"] == target :
            return i

# print(search(ls))
print(searchObj(search_dict, "aji"))


# print({"s" : 32},{"d" : 23})