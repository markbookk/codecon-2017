rotations = input("")
setterName = raw_input("")
lineup = raw_input("")
bench = raw_input("")

lineupA = lineup.split()
benchA = bench.split()

listA = []
listA.append(lineupA[3])
listA.append(lineupA[2])
listA.append(lineupA[1])

listB = []
listB.append(lineupA[4])
listB.append(lineupA[5])
listB.append(lineupA[0])

amountPlayers = benchA[0]

countPlayers = 0
listC =[]
for i in benchA:
	if not(countPlayers == 0):
		listC.append(benchA[countPlayers])
	countPlayers = countPlayers + 1

count = 0


while (count < rotations):
	D = listA[0]
	C = listA[1]
	B = listA[2]
	E = listB[0]
	F = listB[1]
	A = listB[2]

	if not (setterName == listA[2]):
		listB[1] = A
		listB[0] = F
		listB[2] = listC[0]

		listA[0] = E
		listA[1] = D
		listA[2] = C

		listC = listC[1:]
		listC.append(B)
	else:
		listB[2] = B
		listB[0] = F
		listB[1] = A

		listA[0] = E
		listA[1] = D
		listA[2] = C

	count = count + 1


outputA = listA + listB + listC
output = ""
output = listB[2] + " " + listA[2] + " " + listA[1] + " " + listA[0] + " " + listB[0] + " " + listB[1]
print output