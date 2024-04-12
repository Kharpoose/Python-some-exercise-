def string_reverse(str):
    rvs = ''
    
    index = len(str)
    
    while index > 0:
        rvs += str[index - 1]
        
        index = index - 1
        
           
    return rvs


print(string_reverse("deneme 1 2 3 4 5 6"))            