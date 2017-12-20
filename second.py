encrypted = raw_input("")

count = 0
x = 1
y = x + 1
z = y + 1
breakAgain = False
sumResult = 0

while count < 1:
	result = ((x**2) + (y**2) + (z**2))
	if (result == int(encrypted)):
		sumResult = sumResult + x + y + z
	originalX = x
	originalY = y
	originalZ = z
	if (breakAgain == True):
		break
	while (x < 10):
		if ((x <= y) and (y <= z)):
			result = ((x**2) + (y**2) + (z**2))
			if (result == int(encrypted)):
				sumResult = sumResult + x + y + z
		#1,2,3
		if (breakAgain == True):
			break
		while (y < 10):
			if ((x <= y) and (y <= z)):
				result = ((x**2) + (y**2) + (z**2))
				if (result == int(encrypted)):
					sumResult = sumResult + x + y + z
			#1,2,4
			#1,3,5
			#1,4,6
			while (z < 10):
				if ((x <= y) and (y <= z)):
					result = ((x**2) + (y**2) + (z**2))
					if (result == int(encrypted)):
						sumResult = sumResult + x + y + z
				z = z + 1

			z = 1
			y = y + 1
			#1,3,4
			#1,4,5
		y = 1
		z = 1
		x = x + 1
		count = count + 1

print (sumResult)