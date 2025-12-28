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
        if x in j:
            ans.append(i)
    return ans

print(word_contains_index(["abc","bcs","cab","poi"],"a"))