def convertCoin(x) :
    counterCoin = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10,1]
    resList = []
    for i in range(len(counterCoin)) :
        if int(x/counterCoin[i]) > 0 :
            for j in range(int(x/counterCoin[i])) :
                resList.append(counterCoin[i])
                x -= counterCoin[i]
    return resList

intIn = int(input("Input jumlah uang : "))
out = convertCoin(intIn)

print("Output : {0}".format(out))