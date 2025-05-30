def consonant_counter(word):
    """
    Have a function take the string parameter being passed in and return the number of consonants the strings
    contain ie 
    "All cows eat grass " would return 5

    however theres an issue / lack of clarity in the requirements as to whether duplicates are allowed as the totol consonants in the above sentence is 10 and without duplicates, 7. So the function just returns duplicates 
    """

    INVALID_TYPE = "Error: Invalid type entered, must be a string"
    if type(word) != str:
        print(INVALID_TYPE)
        return INVALID_TYPE

    vowels = {
            "a": "a",
            "e": "e",
            "i": "i",
            "o": "o",
            "u": "u",
            }
    freq = 0
    

    # turn everything to a lowercase and remove all white spaces including leading and trailing characters
    fmt_word = word.replace(" ", "").replace("\n", "").replace("\r", "")
    # print(fmt_word.replace("\n", "").replace("\r", ""))

    for char in fmt_word.lower():
        # for punctuation marks, special characters and numbers
        # is.alpha() returns bool
        # if not char.isalpha():
        #     continue
        #
        # if vowels.get(char) is None:
        #     freq += 1

        if vowels.get(char) is None and char.isalpha():
            freq += 1

    
    print(freq)
    return freq


test_1 = "All cows eat grass"
test_2 = " ‘Today is a really hot day but will cool down \n\n\nlater’"
test_3 = " ‘Rabbits bounce whilst dogs bark’"

consonant_counter(test_1)
consonant_counter(test_2)
consonant_counter(test_3)
