def mergesort(list):
	if (len(list) == 1 or len(list) == 0):
		return list
	else: 
		# split the list into two
		left = list[:len(list)//2]
		right = list[len(list)//2:]

		# recursively sort the two halves
		left = mergesort(left)
		right = mergesort(right)

		# merge back together
		return merge(left, right)

def merge(left, right):
	# start looking at the start of both lists
	leftpointer = 0
	rightpointer = 0
	merged_list = []
	
	# as long as both pointers are not at the end of the list...
	while (leftpointer < len(left) and 
		   rightpointer < len(right)):

		# add the smallest element of either list to our output
		if (left[leftpointer] < right[rightpointer]):
			merged_list.append(left[leftpointer])
			leftpointer = leftpointer + 1
		else:
			merged_list.append(right[rightpointer])
			rightpointer = rightpointer + 1
	
	# we may not have finished copying one list, so add it all now
	for leftover_left in left[leftpointer:]:
		merged_list.append(leftover_left)
	for leftover_right in right[rightpointer:]:
		merged_list.append(leftover_right)

	return merged_list


print(mergesort([4,3,2,5,6,1]))
#print(merge([1,3,5], [2,4,6,8]))