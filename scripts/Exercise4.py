def ex4(string):
    string = string.lower()
    result = {}
    for letter in string:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

test_string = 'the quick brown fox jumps over the lazy dog'
print ex4(test_string)
