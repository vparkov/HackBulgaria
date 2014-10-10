def count_consonants(str):
	count = 0 
	consonant = "rtpsdfghjklzxcvbnmRTPSDFGHJKLZXCVBNM"
	for letter in str:
		if letter in consonant:
			count += 1

	return count

print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
