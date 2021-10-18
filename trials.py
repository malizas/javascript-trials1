"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    get_evens = []

    for num in nums:
        if num % 2 == 0:
            get_evens.append(num)
    return get_evens        

def get_odd_indices(items):
    odd_ind = []
    for i in range(len(items)):
        if i % 2 == 1:
            odd_ind.append(items[i])
    
    return odd_ind


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f"{i}. {item}")

        i += 1

def get_range(start, stop):
    nums = []
    i = start
    for i in range(stop):
        nums.append(i)
        i += 1

    return nums


def censor_vowels(word):
    chars = []

    for char in word:
        if char in "aeiou":
            chars.append('*')
        else:
            chars.append(char)
    return "".join(chars)

def snake_to_camel(string):
    camelCase = []
    words = string.split("_")

    for word in words:
        camelCase.extend(f"{word[0].upper()}{word[1:]}")
        # camelCase.append(word)
        # camelCase.append(words[1][0].upper())

    return "".join(camelCase)

def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest

def truncate(string):
    result = []

    for chara in string:
        if len(result) == 0 or chara != result[-1]:
            result.append(chara)
    
    return "".join(result)


def has_balanced_parens(string):
    parens = 0

    for chara in string:
        if chara == "(":
            parens +=1
        elif chara == ")":
            parens -= 1
        if parens < 0:
            return False

    return parens == 0
    

def compress(string):
    compressed = []
    chara_count = 0
    current_chara = ""

    for chara in string:
        if chara != current_chara:
            compressed.append(current_chara)

            if chara_count > 1:
                compressed.append(str(chara_count))

            current_chara = chara
            chara_count = 0
        
        chara_count += 1
    
    compressed.append(current_chara)
    if chara_count > 1:
        compressed.append(str(chara_count))


    return "".join(compressed)
