def count_vowels(str):
	count = 0
	vowels = "aeouiAEOUI"
	for letter in str:
		if letter in vowels:
			count += 1

	return count
print(count_vowels("PyAehon"))