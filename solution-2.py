def merge(arr1, arr2):

	new_arr = []

	i = 0
	j = 0
	len1 = len(arr1)
	len2 = len(arr2)

	while i < len1 and j < len2:

		if arr1[i] < arr2[j]:
			new_arr.append(arr1[i])
			i += 1

		else:
			new_arr.append(arr2[j])
			j += 1

	
	while i < len1:
		new_arr.append(arr1[i])
		i += 1

	
	while j < len2:
		new_arr.append(arr2[j])
		j += 1

	return new_arr

def mergeSort(arr):

	if len(arr) <= 1:
		return arr

	else:

		return merge(mergeSort(arr[0: len(arr)//2]), mergeSort(arr[len(arr)//2: ]))


nlen = raw_input()
arr_in = raw_input()

new_arr = arr_in.split(" ")

for n in range(0, len(new_arr)):
	new_arr[n] = int(new_arr[n])

sortedArr = mergeSort(new_arr)

for m in range(0, len(sortedArr)):
	sortedArr[m] = str(sortedArr[m])

print(" ".join(sortedArr))