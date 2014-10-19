def is_an_bn(word):
    number_of_a = 0
    number_of_b = 0
    position = 0

    length = len(word)
    for i in range(0, length):
        if(word[i] == 'a'):
            number_of_a += 1
            position += 1
        if(word[i] == 'b'):
            break

    for i in range(position, length):
        if(word[i] == 'b'):
            number_of_b += 1
        if(word[i] == 'a'):
            return False

    if number_of_a == number_of_b:
        return True
    return False


print(is_an_bn(""))
print(is_an_bn("rado"))
print(is_an_bn("aaabb"))
print(is_an_bn("aaabbb"))
print(is_an_bn("aabbaabb"))
print(is_an_bn("bbbaaa"))
print(is_an_bn("aaaaabbbbb"))
