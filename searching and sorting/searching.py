#searching
#sequencial search

def sequentialSearch(testlist,key):
    count=0
    found=False
    while count<len(testlist)  and  not found:
        if testlist[count]==key:
            found=True 
        else:
            count+=1
    return found






testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))
#we can optimize sequencial seach using sorted array if key is > item return false:


#Binary Search

def binarySearch(testlist,key):
    start=0
    found=False
    last=len(testlist)-1
    
    while start<=last and not found:
        mid=(start+last)//2
        if testlist[mid]==key:
            found=True
        else:
            if(key<testlist[mid]):
                last=mid-1
            else:
                start=mid+1
    return found
        

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))