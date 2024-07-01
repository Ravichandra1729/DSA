#sorting
#bubbleSort
def bubbleSort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j]>alist[i]:
                alist[j],alist[i]=alist[i],alist[j]
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


#selection sort
def selectionSort(alist):
    
    for i in range(len(alist)-1,0,-1):
        index=0
        for j in range(1,i+1):
            if alist[j]>alist[index]:
                index=j 
        alist[i],alist[index]=alist[index],alist[i]
    return alist
alist1 = [54,26,93,17,77,31,44,55,20]
print(selectionSort(alist1))
        
        
#insertionSort
def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue
    return alist
alist2 = [54,26,93,17,77,31,44,55,20]
    

print(insertionSort(alist2))


#MergeSort

def MergeSort(alist):
    
    return alist

alist3 = [54,26,93,17,77,31,44,55,20]
print("MergeSort:",MergeSort(alist3))


alist4 = [54,26,93,17,77,31,44,55,20]