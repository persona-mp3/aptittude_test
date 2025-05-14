def hamming_dist(str1, str2):
    """
    Hamming distance: have the function take an array of strings, which will only contains two strings of equal length
    and return the number of characters at each position that are different between them. For example->
    ['house', 'hours'], then the program should return 2. Strings will always be of equal length and will only contain lowercase 
    characters.

    test_cases: 
    ['house', 'hours'] -> 2
    [100101001,  110110011] -> should throw an error
    """


    # -> dummy translation -> whenver the strings differ, start counting
    # kind of like a palindrome for each word 
    start = 0
    end = len(str1) - 1
    count =  0

    # uses recursion to comapre the two strings -> str1 and str2
    # and then starts at the first index, where after each iteration the index is moved + 1 
    # the count is tracking the hamming distance function
    calc_hamming_dist(str1, str2,  start, count)


def calc_hamming_dist(word, word2, start, count):
    if start == (len(word) ):
        print(f"hamming distance is -> {count}")
        return count

    if (word[start] != word2[start]):
        # safer to use count = count + 1 bcus of pythons object nature
        count +=1
        # print(f" current hamming distance is -> {count}")
        return calc_hamming_dist(word, word2, start+1, count)


    return calc_hamming_dist(word, word2,  (start+1), count) 

    



def validate_ham_dist(strs):
    # validate against: input, length of array, and length of strings
    INVALID_TYPE = 'Input must be a list of strings'
    INVALID_ARR_TYPE = 'Input must be a list of strings' 
    UNEQUAL_STR = 'Strings must be of the same length'
    INVALID_ARR_LEN = 'Arrays length is invalid, must only contain 2 strings'
    

    str1 = strs[0]
    str2 = strs[1]
    total_len = len(strs)

    if type(strs) != list:
        print(INVALID_ARR_TYPE)
        return INVALID_ARR_TYPE

    if total_len != 2:
        print(INVALID_ARR_LEN)
        return INVALID_ARR_LEN

    if (type(str1) != str or type(str2) != str):
        print(INVALID_TYPE)
        return INVALID_TYPE

    if (len(str1) != len(str2)):
        print(UNEQUAL_STR)
        return UNEQUAL_STR

    print("All validation passed, calculating haming distance")
    hamming_dist(str1, str2)
    

test1 = ['house', 'hours' ]
test2 = [100101001,  110110011]


validate_ham_dist(test2)
