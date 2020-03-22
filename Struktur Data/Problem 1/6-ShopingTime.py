def shoppingTime(memberId, money) :
    if memberId != '' and money != '' :
        old_money = money
        items = [
                ['Sepatu Stacatu', 1500000],
                ['Baju Zoro', 500000],
                ['Baju H&N', 250000],
                ['Sweater Uniklooh',175000],
                ['Casing Handphone', 50000]
                ]
        for i in range(len(items)) :
            for j in range(i, len(items)) :
                if items[i][1] < items[j][1] :
                    temp = items[i]
                    items[i] = items[j]
                    items[j] = temp
        if old_money - items[len(items)-1][1] > 0 :
        # banyak_barang = len(items)-1
            purchased_items = []
            harga = 0
            for i in range(len(items)) :
                if money - items[i][1] >= 0 :
                    money = money-items[i][1]
                    purchased_items.append(items[i][0])
                    harga += items[i][1]

            res = {}
            res['memberId'] = memberId
            res['money'] = old_money
            res['listPurchased'] = purchased_items
            res['changeMoney'] = money

            return res
        else :
            return "Mohon maaf uang tidak cukup"
    else :
        return "Mohon maaf hanya berlaku untuk member saja"

# print(shoppingTime('xsds2sd13', 700000))
print(shoppingTime('xsds2sd13', 3480000))
    



# {{'type' : 'Sepatu', 'brand' : 'Stacatu', 'price' : 1500000},
#         {'type' : 'Baju', 'brand' : 'Zoro', 'price' : 500000},
#         {'type' : 'Baju', 'brand' : 'H&N', 'price' : 250000},
#         {'type' : 'Sweater', 'brand' : 'Uniklooh', 'price' : 175000},
#         {'type' : 'Casing', 'brand' : 'Handphone', 'price' : 50000}}

