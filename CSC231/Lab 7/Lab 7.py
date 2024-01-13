##############
# Name: Tyler Black
# Due Date: 4/14/23
#
# Algorithm: Wrote algorithms for BubbleSort, SelectionSort, InsertionSort, MergeSort, and QuickSort. Answered questions
# about each sorting method in their respective docstring. The questions dealt with runtime, efficiency, usability, and
# expensive operations in the algorithm.
#
# Resources: Dr. Pence and Runestone
################



def BubbleSort(a):
    '''
    Purpose: To sort a list via a BubbleSort Algorithm
    Parameter: A list of integers
    Return: None

    1.) Stable? Yes
    2.) Sort in Place or Extra Memory? Sort in Place
    3.) O(n) is n^2. Worst and best case is n^2. The expensive operations in this algorithm is the double loop and
        "swaps". If the list is in reverse order, this requires the most amount of "swaps".
    4.) Bubble sort is pretty inefficient, so it's rarely used.
        Bubble sort is usually how sorting is conceptually viewed. Can be used easily on linked lists or array based
        lists.
        However, it can be modified to inform the user if the list is already sorted and also cut down the runtime.
        (Smart Bubble Sort)
    '''
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                # temp = a[j]
                # a[j] = a[j + 1]
                # a[j+1] = temp



def SelectionSort(a):
    '''
    Purpose: To sort a list via a Selection Sort Algorithm
    Parameter: A list of integers
    Return: None

    1.) Stable? No
    2.) Sort in Place or Extra Memory? Sort in Place
    3.) O(n) is n^2. Worst and best case is n^2. The expensive operations in this algorithm is the double loop and
        "swaps". If the list is in reverse order, this requires the most amount of "swaps".
    4.) Stable Selection is more efficient than BubbleSort since it can cut down the amount of swaps.
        Only one exchange for every pass through the list. Can be used for linked lists or array based lists.
        However, still not as efficient as other algorithms studied here.
    '''
    for fill_slot in range(len(a)-1, 1,-1):
        pos_of_max = 0
        for j in range(1, fill_slot + 1):
            if a[j] > a[pos_of_max]:
                pos_of_max = j
        temp = a[fill_slot]
        a[fill_slot] =a[pos_of_max]
        a[pos_of_max] = temp




def insertion_sort(a_list):
    '''
    Purpose: To sort a list via an Insertion Sort Algorithm
    Parameter: A list of integers
    Return: None

    1) Stable? Yes
    2) Sort in Place or Extra Memory? Sort in Place
    3) O(n) is n^2. Worst case is n^2, but best case is n. The expensive operations in this algorithm is the
       n+1 comparisons, n copies, and the double loop. If the list is in reverse order, this requires the most amount of
       shifting. If the list is already sorted, it requires only n comparisons.
    4) Insertion Selection is more efficient than BubbleSort and Selection Sort. Since it operates on "shifting" instead
       of "swaps". Shifting cuts down the processing work by 1/3. Can be used easily
       on Array Based Lists and Doubly LinkedLists, but not Singly Linked lists due to absence of the previous instance
       variable. Great for small lists.
       However, still not as efficient as other algorithms studied here.
    '''
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i
        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos = cur_pos - 1
        a_list[cur_pos] = cur_val





def merge_sort(a_list):
    '''
    Purpose: To sort a list via a Merge Sort Algorithm. This algorithm also prints out the process and steps of
             the divide and conquer method.
    Parameter: A list of integers
    Return: None

    1) Stable? Yes
    2) Sort in Place or Extra Memory? Extra Memory
    3) O(n) is nlog(n). Worst case and best case is nlog(n). The expensive operations in this algorithm is the
        recursive divide and conquer and extra n memory. The list is split log(n) times and then merged n times for a
        total nlog(n) runtime.
    4) Merge Sort is the most efficient sorting algorithm studied here. Merge Sort always keeps its nlog(n) runtime
        regardless of the data presented to be sorted. Python sorted() and list.sort(), use a version of MergeSort.
    '''
    print("Splitting", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            print(left_half)
            print(right_half)
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("Merging", a_list)



def quick_sort(a_list):
    '''
    Purpose: To sort a list via a QuickSort Algorithm.
    Parameter: A list of integers
    Return: None

    1) Stable? No
    2) Sort in Place or Extra Memory? Sort in Place
    3) O(n) is n^2. Worst case is n^2, best case is nlog(n). The expensive operations in this algorithm is the
        recursive divide and conquer. Worst case the pivot being used is at the beginning or the end. The best case
        is when the pivot is in the middle of the partition once swapping is finished.
    4) QuickSort is the second most efficient sorting algorithm studied here since Merge Sort always keeps its nlog(n)
        runtime regardless of the data presented to be sorted, but Quick Sort does not. However, on average QuickSort
        is nlog(n). Quick Sort does not need to be used on a list that is already sorted (worst case scenario).
    '''
    quick_sort_helper(a_list, 0, len(a_list) - 1)


def quick_sort_helper(a_list, first, last):
    if first < last:
        split = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split - 1)
        quick_sort_helper(a_list, split + 1, last)


def partition(a_list, first, last):
    pivot_val = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            left_mark = left_mark + 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = (
                a_list[right_mark],
                a_list[left_mark],
            )
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    return right_mark




def main():
    print('Practice sorting via Bubble sort')
    print(BubbleSort.__doc__)
    lst = [1, 0, 7, 6, 3, 9, 10]
    BubbleSort(lst)
    print(f'The list [1, 0, 7, 6, 3, 9, 10] sorted should be [0, 1, 3, 6, 7, 9, 10]: {lst}')
    print()

    print('Practice sorting via Selection Sort')
    print(SelectionSort.__doc__)
    lst2 = [1, 0, -1, 2, 4, 7, 5, 10]
    SelectionSort(lst2)
    print(f'The list [1, 0, -1, 2, 4, 7, 5, 10], should be [-1, 0, 1, 2, 4, 5, 7, 10]: {lst2}')
    print()

    print('Practice sorting via Insertion Sort')
    print(insertion_sort.__doc__)
    lst3 = [0, 7, 2, -1, -70, 2, 10, 11]
    insertion_sort(lst3)
    print(f'The list [0, 7, 2, -1, -70, 2, 10, 11] sorted should be [-70, -1, 0, 2, 2, 7, 10, 11]: {lst3}')
    print()

    print('Practice sorting via Merge Sort')
    print(merge_sort.__doc__)
    print()
    lst4 = [0, -1, 7, 5, 4, 10, 9, 7, 12]
    lst6 = [0,-1]
    merge_sort(lst4)
    merge_sort(lst6)
    print()
    print(f'The list [0, -1, 7, 5, 4, 10, 9, 7, 12] sorted should be [-1, 0, 4, 5, 7, 7, 9, 10, 12]: {lst4}')
    print()
    print(lst6)
    print()

    print('Practice sorting via QuickSort')
    print(quick_sort.__doc__)
    lst5 = [0, -1, 9, 8, 5, -25, 0, 5, 10]
    quick_sort(lst5)
    print(f'The list [0, -1, 9, 8, 5, -25, 0, 5, 10] sorted should be [-25, -1, 0, 0, 5, 5, 8, 9, 10]: {lst5}')


main()