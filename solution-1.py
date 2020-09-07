
import pdb


def mergeSort(arr1, len1, arr2, len2):

	#pdb.set_trace()
	new_arr = []

	i = 0
	j = 0

	while i < len1 and j < len2:

		if arr1[i] < arr2[j]:
			new_arr.append(arr1[i])
			i += 1

		else:
			new_arr.append(arr2[j])
			j += 1

	if i < len1:
		while i < len1:
			new_arr.append(arr1[i])
			i += 1

	else:
		while j < len2:
			new_arr.append(arr2[j])
			j += 1

	return new_arr

# variables for mergeSort params
arr1 = [];
len1 = 0;
arr2 = [];
len2 = 0;

# Gets two different inputs

for input_in in range(0, 2):
	new_in = raw_input()

	# change to array of strings 
	in_arr = new_in.split(" ")

	# cast each number to int
	for in_arr_ind in range(0, len(in_arr)):
		in_arr[in_arr_ind] = int(in_arr[in_arr_ind])

	# set appropriate parameters depending on whether it's the first or second line
	if input_in == 0:
		len1 = in_arr[0]

		# remove first element (length of array)
		in_arr.remove(in_arr[0])

		arr1 = in_arr

	else:
		len2 = in_arr[0]

		in_arr.remove(in_arr[0])

		arr2 = in_arr

# set merged array
merged = mergeSort(arr1, len1, arr2, len2)

# add length to beginning
merged.insert(0, len1+len2)

# convert elements to strings
for str_in in range(0, len(merged)):
	merged[str_in] = str(merged[str_in])

# print output in string form
print(" ".join(merged))






