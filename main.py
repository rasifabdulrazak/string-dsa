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

#Valid Palindrome
def valid_palindrome(word:str):
    wo = "".join([char for char in word if char.isalnum()])
    og = wo.lower()
    return og == og[::-1]


print(valid_palindrome("A man, a plan, a canal: Panama"))
    
def valid_palindrome_2_pointer(word:str):
    word = word.lower()
    i = 0
    j = len(word) - 1
    while i < j:
        if not word[i].isalnum(): 
            i += 1
        elif not word[j].isalnum(): 
            j -= 1
        elif word[i] == word[j]:
            i += 1
            j -= 1
        else: return False
    return True

print(valid_palindrome_2_pointer("A man, a plan, a canal: Panama"))

def largest_odd_number(num:str):
    n = len(num) - 1
    while n >= 0:
        if int(num[n]) % 2 == 1:
            return num[0:n+1]
        n -= 1
    return ""

print(largest_odd_number("4322"))  

def longest_common_prefix(words:list):
    if not words: return ""
    prefix = words[0]
    print(prefix)
    for s in words[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

print(longest_common_prefix(["flower","flow","flight"]))