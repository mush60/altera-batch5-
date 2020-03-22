def test(words) :
    klist = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
    res = []
    for i in words :
        j = i.lower()
        for kbr in klist :
            count = 0
            for let in j :
                if let not in kbr :
                    count += 1
            if count < 1 :
                res.append(i)

    return res


print(test(["Hello","Alaska","Dad","Peace"]))