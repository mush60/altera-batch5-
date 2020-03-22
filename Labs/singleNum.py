def counts(listn) :
    for i in listn :
        if listn.count(i) == 1 :
            return i

    # x = {i: listn.count(i) for i in listn}
    # for n in x :
    #     if x[n] == 1 :
    #         return n
    # y = x.get[]

listn = [5, 2, 3, 3, 3, 3, 5]
print(counts(listn))

