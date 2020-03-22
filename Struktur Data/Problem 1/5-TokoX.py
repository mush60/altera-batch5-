def countProfit(shoppers) :
    listBarang = [
        ['Sepatu Stacattu', 1500000, 10],
        ['Baju Zoro', 500000, 2],
        ['Sweater Uniklooh', 175000, 1]
    ]

    res = []
    for p in listBarang :
        subRes = {}
        product = p[0]
        pembeli = []
        leftOver = p[2]
        totalProfit = 0
        
        for s in shoppers :
            if s['product'] == product :
                if leftOver - s['Amount'] >= 0 :
                    pembeli.append(s['name'])
                    leftOver = leftOver - s['Amount']
                    totalProfit = totalProfit + (p[1] * s['Amount'])
                subRes = {
                    'product' : product,
                    'shoppers' : pembeli,
                    'leftOver' : leftOver,
                    'totalProfit' : totalProfit
                }
        res.append(subRes)
    return res

print(countProfit([
                    {'name' : 'Windi', 'product' : 'Sepatu Stacattu', 'Amount' : 5},
                    {'name' : 'Vanessa', 'product' : 'Sepatu Stacattu', 'Amount' : 6},
                    {'name' : 'Rani', 'product' : 'Sweater Uniklooh', 'Amount' : 2}
                    # {'name' : 'Windi', 'product' : 'Sepatu Stacattu', 'Amount' : 8},
                ]))


    # itemSale = {
    #     'Sepatu' : {
    #         'brand' : 'Stacattu',
    #         'harga' : 1500000,
    #         'stock' : 10
    #     }, 
    #     'Baju' : {
    #         'brand' : 'Zoro',
    #         'harga' : 500000,
    #         'stock' : 2
    #     },
    #     'Sweater' : {
    #         'brand' : 'Uniklooh',
    #         'harga' : 175000,
    #         'stock' : 1
    #     }
    # }