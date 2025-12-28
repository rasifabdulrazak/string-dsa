# String DSA Questions


# Given a string s consisting of words and spaces, return the length of the last word in the string.
def count_of_last_word(word):
    length = len(word) - 1
    coun = 0
    for i in range(length,-1,-1):
        if word[i] != " ":
            coun += 1
            
        elif coun > 0:
            break
        else:
            continue        
        
    return coun
    
print(count_of_last_word("Hello world"))

# Find Words Containing Character
def word_contains_index(words:list,x:str):
    ans = []
    for i,j in enumerate(words):
        for char in j:
            if char == x:
                ans.append(i)
                break
    return ans

print(word_contains_index(["leet","code","cab","poi"],"a"))

# Jewels and Stones
def jwels_and_stones(jewel:str,stones:str):
    count  = 0
    for i in stones:
        if i in jewel:
            count+=1
    return count

print(jwels_and_stones("aA","aAAbbbb"))