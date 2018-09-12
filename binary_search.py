def binary_search(array, target):
	lower = 0 
	upper = len(array)
	while lower < upper:
		x = lower + (upper - lower) // 2
		val = array[x]
		if target == val:
			return x 
		elif target > val:
			if lower == x:
				break 
			lower = x 
		elif target < val:
			upper = x

y = [5,6,7,8,9]

print binary_search(y, 3)