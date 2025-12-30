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

# Find Most Frequent Vowel and Consonant
def freq_count_vowel(word):
    vowel = ['a','e','i','o','u']
    count = {}
    max_vowel = 0
    max_cons = 0
    
    for char in word:
        count[char] = count.get(char,0) + 1
        
    for key,value in count.items():
        if key in vowel and count[key] > max_vowel:
            max_vowel = count[key]
        elif key not in vowel and count[key] > max_cons:
            max_cons = count[key]
            
    return max_cons + max_vowel

print(freq_count_vowel("successses"))


# Split a String in Balanced Strings
def split_balanced_string(word:str):
    l = 0
    r = 0
    count = 0
    for i in word:
        if i =='R':
            r += 1
        else:
            l += 1
        if l == r:
            count += 1
            l = r = 0
    return count

print(split_balanced_string("RRLLL"))

def split_balanced_string_one_var(word:str):
    var = 0
    count = 0
    
    for i in word:
        if i == "R":
            var += 1
        else:
            var -= 1
            
        if var == 0:
            count += 1
            
    return count

print(split_balanced_string_one_var("RLRL")) 