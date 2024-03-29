def merge_sert(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        leftside = list1[:mid]
        rightside = list1[mid:]


        merge_sert(leftside)
        merge_sert(rightside)

        i,j,k = 0,0,0
        while i < len(leftside) and j < len(rightside):
            if leftside[i] <= rightside[j]:
                list1[k] = leftside[i]
                i = i + 1
            else:
                list1[k] = rightside[j]
                j += 1
            k += 1

        while i < len(leftside):
            list1[k] = leftside[i]
            i+=1
            k+=1

        while j < len(rightside):
            list1[k] = rightside[j]
            j+=1
            k+=1

def insert_sort(list1):
    for i in range (1,len(list1)):
        cur_index = i
        cur_val = list1[i]
        while cur_index > 0 and cur_val <= list1[cur_index-1]:
            list1[cur_index] = list1[cur_index-1]
            list1[cur_index-1] = cur_val
            cur_index -= 1


def rec_max(list1):
    if len(list1) == 1:
        return list1[0]
    else:
        result = rec_max(list1[1:])
        if result >= list1[0]:
            return result
        else:
            return list1[0]


def insert_sort_book(list1):
    for i in range(1,len(list1)):
        key = list1[i]
        j = i - 1
        while list1[j] > key and j >= 0:
            list1[j+1] = list1[j]
            j-=1
        list1[j+1] = key

list2 = [9,7,-1,0]
list3=[9,-7,-5,6,3]
list4 = [0,-2,9,8,10]
merge_sert(list2)
insert_sort(list3)
print(list3)
print(list2)
print(rec_max(list3))
print()
insert_sort_book(list4)
print(list4)


