import random

def Random(small,large,length):
    randomlist = []
    for i in range(length):
        randomlist.append(random.randint(small,large))
    return randomlist

def BubbleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list,FindMiddle(list)

def Merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result .append(left.pop(0))
        else:
            result .append(right.pop(0))
    result  = result  + left + right
    return result 

def MergeSort(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left = MergeSort(list[:mid])
    right = MergeSort(list[mid:])
    return Merge(left,right)

def QuickSort(list,left,right):
    i = left 
    j = right
    if i >= j:
        return list
    key = list[i]
    while i < j:
        while i < j and list[j] >= key:
            j = j-1                                                             
        list[i] = list[j]
        while i < j and list[i] <= key:    
            i = i+1 
        list[j] = list[i]
    list[i] = key 
    QuickSort(list, left, i-1)
    QuickSort(list, j+1, right)
    return list,FindMiddle(list)

def FindMiddle(list):
    M = len(list)//2
    if (len(list) % 2) == 0:
        return (list[~M],list[M])
    else:
        return list[M]

def Median(list):
    M = len(list) // 2
    return (list[M] + list[~M]) / 2

"""
def Median(L): 
    C = Copy(L)
    Sort(C) 
    return ElementAt(C,GetLength(C)//2)
"""

a = [1,5,4,7,8,3,6,11,21]
b = [9,5,3,0,4,6,5,7]
c = [10,60,54,87,52,1,2,36,54,21]

Listone = Random(0,10, 9)
print(Listone)

print(BubbleSort(Listone))
#Toprint = MergeSort(Listone)
#print(MergeSort(Listone))
#print(QuickSort(Listone,0,8))
print(Median(Listone))
#print(FindMiddle(Toprint))
