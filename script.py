import math
from typing import List, Optional


# question 1
def first_factorial(params: int) -> int:
    if type(params) != int:
        error_msg = f'Invalid value passed of type: {type(params)}, you must enter an integer'
        return error_msg
    
    if params < 0:
        error_msg = f'Value passed must not be less than 0, you entered: {params} '
        return error_msg
    
    
    total_factorial = 1
    
    # add one to make factorial inclusive
    n = params + 1
    
    for i in range(n):
        if i == 0:
            continue
        # print(i)
        
        total_factorial = total_factorial *  i
    
    return total_factorial
    


# question 2
def time_conversion(params: int) -> str:
    
    if type(params) != int:
        error_msg = f'You passed in a {type(params)}, you must pass in an integer'
        return error_msg


    # if value passed is less than 0
    if params <= 0:
        error_msg = 'Number must be positive'
        return error_msg
    
    one_hour = 60
    no_of_hours = params / one_hour
    
    # round to nearest whole number 
    no_of_hours = math.floor(no_of_hours)
    
    # remainder as minutes
    minutes = params % one_hour
    
    time_converted = f'{no_of_hours}:{minutes}'
    
    return time_converted


# question 3
def consonant_counter(word: str) -> int:
    if type(word) != str:
        error_msg = f'Invalid entry, must be of type str, you entered {type(word)}'
        return error_msg
    
    
    consonant_len: list[str] = []
    filtered_list: list[str] = []
    
    edge_cases: list[str] = [
                '/', '.', '`', '+', '-', '(', ')', ']', 
                '[', '{', '}', '%', '£', '#', '!', '@', 
                '"', '^','<', '>', ':',';', ' ', "'", 
                '*', '’','‘', '=']
    
    
    word = word.lower()
    
    for char in word:
        if char in 'aeiou':
            continue
        
        if char in edge_cases:
            continue
        
        if char in '1234567890':
            continue
        
        consonant_len.append(char)
        
    # print('With doubles', consonant_len , len(consonant_len))
        

    for char in consonant_len:
        # check if char is already in filtered list
        if char in filtered_list:
            continue
        
        filtered_list.append(char)
    
    # print('Without doubles', filtered_list , len(filtered_list))
    
    
    return len(filtered_list)

# question 4
def hamming_dist(params: list[str]) -> int:
    
    user_words: list[str] = []
    
    if type(params) != list:
        case_01 = f'You entered a value of type {type(params)} instead of a list'
        print('Value passed must be a list')
        return case_01
    
    if len(params) != 2:
        case_02 = f'List must contain two strings, you entered a list containing {len(params)} items'
        return case_02
    
    for i in params:
        if type(i) != str:
           case_03 = f'Both values must be a string'
           return case_03
       
        user_words.append(i)
    
    word_1 = user_words[0]
    word_2 = user_words[1]
    
    if len(word_1) != len(word_2):
        case_04 = f'Two values must be of equal length'
        return case_04
    
    
    different_characters = []
    
    for x in range(len(word_1)):
        if word_1[x] != word_2[x]:
            # print(word_1[x])
            different_characters.append(word_1[x])
    
    hamming_distance = len(different_characters)
    
    return hamming_distance
    
       
# question 5
def roman_numerals(params: int)-> str:
    
    if type(params) != int:
        error_msg = f'Input must be an integer, you entered {type(params)}'
        return error_msg
    
    if params > 4000 or params <= 0:
        error_msg = f'Input must be between 0 and 40000, you entered {params}'
        return error_msg



    print('here')

















# test_factorial = first_factorial(0)
# print(test_factorial)
# print(type(test_factorial))


# test_time_conversion = time_conversion(74)
# print(test_time_conversion)


# test_consonant_counter = consonant_counter("All cows eat grass") 
# returns 7 without doubles, 10

# test_consonant_counter = consonant_counter("‘Rabbits bounce whilst dogs bark’") 
# returns 12 without doubles, 19

# test_consonant_counter = consonant_counter("‘Rabbits bounce whilst dogs bark1234567890’") 
# print(test_consonant_counter)

    
# test_case_1: list[str] = ['house', 'hours']
# returns 2

# test_case_2: list[str] = ['100101001', '110110011']
# returns 4

# test_case_3: list[str] = ['11001101', '10110110']
# returns 6

# test_case_4: list[str] = ['1100110144j', '10110110']
# error message

# test_case_5: list[str] = [0, '10110110']
# error message

# test_case_6: list[str] = None


# test_hamming_dist = hamming_dist(test_case_6)
# print(test_hamming_dist)




