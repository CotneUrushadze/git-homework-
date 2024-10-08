def how_manny_letters(word):
    dict = {}
    for i in word:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
            
    return dict

print(how_manny_letters("hello"))
