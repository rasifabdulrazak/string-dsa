# String DSA Questions


# Given a string s consisting of words and spaces, return the length of the last word in the string.
def count_of_last_word(word):
    length = len(word) - 1
    coun = 0
    for i in range(length,-1,-1):
        print(i,"========")
        if word[i] != " ":
            print(word[i])
            coun += 1
        elif coun > 0:
            break
        else:
            continue
        print(coun,"=========")
        
        
    return coun
        
        
    
    
print(count_of_last_word("Hello world"))