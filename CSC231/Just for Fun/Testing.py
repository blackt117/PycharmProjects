def add5 (x,y):
    for i in range(len(y)):
        if y[i] not in x:
            x[y[i]] = 1
        else:
            x[y[i]] += 1


    return False



def maxdef (x):
    maxd = 0
    index_max = 0
    index_list = 0
    list_keys = list(x.keys())
    list_values = list(x.values())
    for i in x:
        if x[i] > maxd:
            maxd = x[i]
            index_max = index_list
        index_list +=1
    return list_keys[index_max]
x = {}
y = [1,2,3,4,65,6,4,3,2,1,7,8,1]
add5(x,y)
print(x)
print(maxdef(x))
print(x)