def mostFrequent(items) :
    item_lite = list(set(items))
    # sorting_item :
    for i in range(len(items)) :
        for j in range(len(items)) :
            if items.count(items[i]) > items.count(items[j]) :
                temp = items[i]
                items[i] = items[j]
                items[j] = temp
    # while
    # return items
    res = ''
    for item in item_lite :
        res += item+'('+str(items.count(item))+'),'

    # item_lite = {}
    # for item in items :
    #     if item not in item_lite :
    #         item_lite[item] = 1
    #     else : 
    #         item_lite[item] += 1
    
    # stringitem = str(item_lite).replace('}','').replace('{','').replace("': ", '(').replace(", '", '), ')+")'"
    # return stringitem
    return "'"+res[:-1]+"'"

print(mostFrequent(['asus', 'samsung', 'asus', 'iphone', 'iphone', 'asus', 'xiaomi']))