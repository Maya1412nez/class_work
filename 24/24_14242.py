def commonChars(words):
    d = dict()
    for j in range(len(words)):
        for let in words[j]:
            if all(let in word for word in words):
                if j not in d:
                    d[j] = []
                d[j].append(let)

    def intersection_list(list1, list2): 
        list3 = []
        for el in list2:
            # print(list2, el, el in list2)
            if el in list2:
                list3.append(el) 
        return list3 
    alph = list('qwertyuiopasdfghjklzxcvbnm')
    for values in d:
        print(d[values], alph)
        alph = intersection_list(alph, d[values])
    return alph


print(commonChars(["cool","lock","cook"]))