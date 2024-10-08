def reverse(word):
    reversed = []

    for i in word:
        reversed.insert(0, i)
        
    result = "".join(reversed)
    return result
        
    
print(reverse("reverse"))