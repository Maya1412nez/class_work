for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (y <= (not(x <= z))) or w 
                f1 = (y <= (x > z)) or w 
                if f == 0 and f1 == 0:
                    print(x, z, y, w, f)

''' w = 0 
(y <= (x > z)) = 0 при (x > z) = 0
или при (x <= z)

'''