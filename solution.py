def binarySearch(arr, ind, start, end):
    if(int((start+end)/2) < 0):
        return -1 
    elif(arr[int((start+end)/2)][1] <= arr[ind][0] and arr[ind][0] < arr[int((start+end)/2)+1][1]):
        return int((start+end)/2)
    elif(arr[ind][0] < arr[int((start+end)/2)][1] and end > 0):
        return binarySearch(arr, ind, start, int((start+end)/2))
    elif(arr[ind][0] >= arr[int((start+end)/2)+1][1]):
        return binarySearch(arr, ind, int((start+end)/2)+1, end)
    else:
        return -1 

def sortReturn(elem):
    return elem[1]

def findJobs(n, arr):
    arr.sort(key=sortReturn)
    fin = []
    for i in range(0, n+1):
        fin.append(0)
    pre = []
    for k in range(0, n):
        index = binarySearch(arr, k, 0, k-1)
        pre.append(index)
        fin[k+1] = max(fin[k], fin[pre[k]+1]+arr[k][2])
    return fin[n]

n = int(input())
arr = []
for i in range(0, n):
    inputStr = input()
    arrIndex = [int(x) for x in inputStr.split()]
    arr.append(arrIndex.copy())
       
ans = findJobs(n, arr)
print(str(ans))

