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



list2 = [9,7,-1,0]
list3=[9,-7,-5,6,3]
merge_sert(list2)
insert_sort(list3)
print(list3)
print(list2)


