import math
from typing import List, Optional



def first_factorial(params: int) -> int:
    """
    Question 1:
    First Factorial Have the function take the number parameter being passed and return the factorial of it. 
    For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, 
    the range will be between 1 and 18 and the input will always be an integer
    """
    if type(params) != int:
        error_msg = f'Invalid value passed of type: {type(params)}, you must enter an integer'
        return error_msg
    
    if params < 0:
        error_msg = f'Value passed must not be less than 0, you entered: {params} '
        return error_msg
    
    # setting an incremental product total to 1 for the for loop
    total_factorial = 1
    
    
    # since the range method is exclusive, we'll need to add 1 to the passed in value
    # if parmas = 5, range(params) = 0, 1, 2, 3, 4
    # n = params + 1 = range(params) = 0, 1, 2, 3, 4, 5
    n = params + 1
    
    
    for i in range(n):
        if i == 0:
            continue
        # print(i)
        
        total_factorial = total_factorial *  i
    
    return total_factorial
    


<<<<<<< HEAD

test_factorial = first_factorial(4)
# print(test_factorial)







# function return value should be of type of string
=======
# function value should be of type of string
>>>>>>> b9807fdf752ca144039e9ccc4aac8f3bb6699cb5
def time_conversion(params: int) -> str:
    """
    Question 2: 
    Have the function take the number parameter being passed and return the number of hours and minutes 
    the parameter converts to (ie. if num = 63 then the output should be 1:3). 
    Separate the number of hours and minutes with a colon.
    For the test cases, the numbers used will be 74 and 118
    """
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


test_time_conversion = time_conversion(63)
# should return 1:3
test_time_conversion_2 = time_conversion(74)
# should return 1:14
test_time_conversion_3 = time_conversion(118)
# should return 1:58
test_time_conversion_4 = time_conversion(None)
# should return error message


print('convert 3', test_time_conversion_4)











# function should return an interger type value
def consonant_counter(word: str) -> int:
    """
<<<<<<< HEAD
    Question 3:
=======
    Question:
>>>>>>> b9807fdf752ca144039e9ccc4aac8f3bb6699cb5
    Have the function take the string parameter being passed and return the number of 
    consonants the string contains (ie. "All cows eat grass" would return 5).
    For the test cases the two strings will be ‘Today is a really hot day but will cool
    down later’ and also ‘Rabbits bounce whilst dogs bark’

    """
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
    
    # converts all words to lowercase
    word = word.lower()
    
    # iterate through the word the user entered
    # if any character in the word is a vowel, number or any edgecase, skip it
    # else append to consonant_len list
    for char in word:
        if char in 'aeiou':
            continue
        
        if char in edge_cases:
            continue
        
        if char in '1234567890':
            continue
        
        consonant_len.append(char)
        
    # print('With doubles', consonant_len , len(consonant_len))
        
    # iterate through the cosonant_len array and append to filtered_list array
    # if a character from the consonnant_len array already exists in the filtered list array, skip it
    # then returned the len of the filtered array as the number of consonants

    for char in consonant_len:
        # check if char is already in filtered list
        if char in filtered_list:
            continue
        
        filtered_list.append(char)
    
    # print('Without doubles', filtered_list , len(filtered_list))
    
    
    return len(filtered_list)



test_consonant_counter_1 = consonant_counter("All cows eat grass") 
# returns 7 without doubles, 10 with doubles

test_consonant_counter_2 = consonant_counter("‘Rabbits bounce whilst dogs bark’") 
# returns 12 without doubles, 19 with doubles

test_consonant_counter_3 = consonant_counter("‘Rabbits bounce whilst dogs bark1234567890’") 
# print(test_consonant_counter_1)









# function should return a value of type int
def hamming_dist(params: list[str]) -> int:
    
    """
    Question 4:
    Have the function take the array of strings, which will only contain two strings of equal length 
    and return the number of characters at each position that are different between them. 
    For example: [“house”, “hours”] then your program should return 2. 
    The string will always be of equal length and will only contain lowercase characters from the alphabet and numbers.
    For the test cases, the first set of numbers will be [100101001 and 110110011] and [11001101 and 10110110]

    """
    user_words: list[str] = []

    """
    Have the function take the array of strings, which will only contain two strings of equal length 
    and return the number of characters at each position that are different between them. 
    For example: [“house”, “hours”] then your program should return 2. 
    The string will always be of equal length and will only contain lowercase characters from the alphabet and numbers.
    For the test cases, the first set of numbers will be [100101001 and 110110011] and [11001101 and 10110110]

    """
    
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
    
    # strings in the array/list
    word_1 = user_words[0]
    word_2 = user_words[1]
    
    if len(word_1) != len(word_2):
        case_04 = f'Two values must be of equal length'
        return case_04
    
    
    different_characters = []

    # since the two words in the string must be of the same length, we can match the index in a for loop
    # to be able to match the index for each iteration in a for loop, the range method was used
    # the len of the string was passed in as a parameter for the range method 
    # range is inclusive of 0 and exclusive of the last digit, making it suitable
    # if len = 5, range(len) will be 0, 1, 2, 3, 4
    # which is perfect for pythons index matching system

    # to get the number of indices at which the characters differ
    # we can push them into an arrray/list and determine the length of the array

    # x represents the index
    for x in range(len(word_1)):
        if word_1[x] != word_2[x]:
            # print(word_1[x])
            different_characters.append(word_1[x])
    
    hamming_distance = len(different_characters)
    
    return hamming_distance
    

test_case_1: list[str] = ['house', 'hours']
# returns 2

test_case_2: list[str] = ['100101001', '110110011']
# returns 4

test_case_3: list[str] = ['11001101', '10110110']
# returns 6

test_case_4: list[str] = ['1100110144j', '10110110']
# error message

test_case_5: list[str] = [0, '10110110']
# error message

test_case_6: list[str] = None


test_hamming_dist = hamming_dist(test_case_6)
print(test_hamming_dist)








<<<<<<< HEAD
# function should return a str
=======
# question 5
>>>>>>> b9807fdf752ca144039e9ccc4aac8f3bb6699cb5
def roman_numerals(params: int)-> str:
    """
    Question 5:
    Have the function take in an integer value of up to 4000 and then convert that number into the correct 
    Roman numeral equivalent. For example if the function takes 1943 then the return should be MCMXLIII
    For the test cases, the two numbers will be 3612 and 423
    
    """
    
    if type(params) != int:
        error_msg = f'Input must be an integer, you entered {type(params)}'
        return error_msg
    
    if params > 4000 or params <= 0:
        error_msg = f'Input must be between 0 and 40000, you entered {params}'
        return error_msg



    print('here')



<<<<<<< HEAD
=======














# test_factorial = first_factorial(0)
# print(test_factorial)
# print(type(test_factorial))



    




>>>>>>> b9807fdf752ca144039e9ccc4aac8f3bb6699cb5
