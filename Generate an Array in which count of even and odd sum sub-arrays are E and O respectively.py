# Python 3 implementation of the approach

# Function to generate and print
# the required array
def CreateArray(N, even, odd):
	temp = -1
	
	# Find the number of odd prefix sums
	for i in range(N + 2):
		if (i * ((N + 1) - i) == odd):
			temp = 0
			OddPreSums = i
			break

	# If no odd prefix sum found
	if (temp == -1):
		print(temp)
	else:
		
		# Calculating the number
		# of even prefix sums
		EvenPreSums = (N + 1) - OddPreSums
		e = 1
		o = 0

		# Stores the current prefix sum
		CurrSum = 0
		for i in range(N):
			
			# If current prefix sum is even
			if (CurrSum % 2 == 0):
				
				# Print 0 until e = EvenPreSums - 1
				if (e < EvenPreSums):
					e += 1
					print("0 ", end = "")
				else:
					o += 1

					# Print 1 when e = EvenPreSums
					print("1 ", end = "")
					CurrSum += 1
	
			else:
				if (e < EvenPreSums):
					e += 1
					print("1 ")
					CurrSum += 1
				else:
					o += 1

					# Print 0 for rest of the values
					print("0 ", end = "")
		print("\n", end = "")

# Driver code
if __name__ == '__main__':
	N = 15
	even = 60
	odd = 60
	CreateArray(N, even, odd)

# This code is contributed by
# Surendra_Gangwar
