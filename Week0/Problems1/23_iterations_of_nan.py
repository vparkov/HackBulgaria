def iterations_of_nan_expand(expand):
    not_a = "Not a "
    answer = expand.count(not_a)
    if answer == 0 and len(expand) > 1:
        return False
    return answer

print(iterations_of_nan_expand("Show these people!"))
