"""
File: Inversions.py
-----------------------
This program implements inversions for an array defined
within the program.
"""

import sys
import operator
import os
import math
import string
import random

def inversions(array, counter):
	size = len(array)
	if size == 0 or size == 1:
		return (array, counter)
	output_array = []
	array_presort_one = []
	array_presort_two = []
	array_one = []
	array_two = []
	
	for i in range(size/2):
		array_presort_one.append(array[i])
	for j in range(size - size/2):
		array_presort_two.append(array[size / 2 + j])

	array_one, counter = inversions(array_presort_one, counter)
	array_two, counter = inversions(array_presort_two, counter)

	i = 0
	j = 0

	for k in range(size):
		if i >= len(array_one) and j < len(array_two):
			output_array.append(array_two[j])
			j += 1
		else:
			if j >= len(array_two) and i < len(array_one):
				output_array.append(array_one[i])
				i += 1
			else:
				if i < len(array_one) and j < len(array_two) and array_one[i] < array_two[j]:
					output_array.append(array_one[i])
					i += 1
				else:
					if i < len(array_one) and j < len(array_two):
						output_array.append(array_two[j])
						if array_one[i] > array_two[j]:
							counter += len(array_one) - i
						j += 1
	return (output_array, counter)

def main(args):
    try:
        # Defining the array
        user_array = []
        final_array = []
        counter = 0
        n = 10000
        maxnum = 100000
        for i in range(n):
        	user_array.append(maxnum - i * maxnum * 2 / n)
        	# user_array = [40, 3, 24, 1245, 2, -43, 20, 132, 49, 0, 1, 15, 23, 58, 1, 4, -1, -1, 4, 8, 242, 12]        
        
        final_array, counter = inversions(user_array, 0)
        print final_array
        print counter

    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        return 1
    else:
        return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))

