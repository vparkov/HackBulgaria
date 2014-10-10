import math	

people = [2, 3, 6, 4, 6, 4]

for i in range(0,len(people)):
	print(people[i])

print("\n")

for person in people:
	print(person)

print("\n")

for index, person in enumerate(people):
	print(index, person)