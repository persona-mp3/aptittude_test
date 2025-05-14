"""
Have a function take an interger value up to 4000 and then convert that number into the correct Roman numeral
equivalent. For example, if the fn takes 1943 then the return should be MCMXLIII

test cases -> 3612 423
"""

# so we want to check the length of the digit, that way, we can quicly determine the measurement:
# if len = 2 -> tens, 
# if len = 3 -> hundreds, 
# if len = 4 -> thousands

# rules
# a letter cannot be repeated more than 3 times'
# in a scenario after the 3rd letter, the next number should be the single unit + the next unit ie 
# lxxx -> 80 , we want to get 90, but we know 100 is C to 90 -> XC

# so we also need to the computer to read it in terms of units and tenths sequence 
# so depending on the length of the string, we can then read it to get the roman numerals
# so we can make a set of dictionaries for each scenario that there will be lookups for each section
# 3233 -> 3 will be searched for in thousands dict , 2 in hundreds dict, 3 in tens and so on
# 3000 +200 + 30 + 3

def calc_unit(coerced_str, units):
    unit = coerced_str[0]
    result = ""
    result += units[unit]
    print(f"{coerced_str} to roman numerals -> {result}")
    return result


def calc_tens(coerced_str, units, tens):
    tenth = coerced_str[0]
    unit = coerced_str[-1]
    result = ""
    result += tens[tenth]
    result += units[unit]
    print(f"{coerced_str} to roman numerals -> {result}")
    return result

    
def calc_hundreds(coerced_str, units, tens, hundreds):
    hundredth = coerced_str[0]
    tenth = coerced_str[1]
    unit = coerced_str[-1]
    result = ""
    result += hundreds[hundredth]
    result += tens[tenth]
    result += units[unit]

    print(f"{coerced_str} to roman numerals -> {result}")
    return result

def calc_thousands(coerced_str, units, tens, hundreds, thousands):
    print("Calculating thousands...")
    thousandth = coerced_str[0]
    hundredth = coerced_str[1]
    tenth = coerced_str[2]
    unit = coerced_str[-1]

    result = ""
    result += thousands[thousandth]
    result += hundreds[hundredth]
    result += tens[tenth]
    result += units[unit]
    # print (result)
    print(f"{coerced_str} to roman numerals -> {result}")
    return result

def roman_numeral(num):
    if type(num) != int:
        print("Input must be an integer")
        return 'Input must be an interger'

    if num > 4000 or num < 1:
        print("Input must be within the range of 1 and 4000")
        return
    
    units = {
            "0": "",
            "1": "I",
            "2": "II",
            "3": "III",
            "4": "IV",
            "5": "V",
            "6": "VI",
            "7": "VII",
            "8": "VIII",
            "9": "IX",
            }
    tens = {
            "0": "",
            "1": "X",
            "2": "XX",
            "3": "XXX",
            "4": "XL",
            "5": "L",
            "6": "LX",
            "7": "LXX",
            "8": "LXXX",
            "9": "XC",
            }

    hundreds = {
            "0": "",
            "1": "C",
            "2": "CC",
            "3": "CCC",
            "4": "CD",
            "5": "D",
            "6": "DC",
            "7": "DCC",
            "8": "DCCC",
            "9": "CM"
            }

    thousands = {
            "0": "",
            "1": "M",
            "2": "MM",
            "3": "MMM",
            "4": "Δ",
            }
    coerced_str = str(num)
    str_len = len(coerced_str)

    match str_len:
        # theres a strange edge case here when 0000 is coereced to a str, the length is 1
        case 1:
            return calc_unit(coerced_str, units) 

        case 2:
             return calc_tens(coerced_str, units, tens) 

        case 3:
            return calc_hundreds(coerced_str, units, tens, hundreds) 

        case 4:
            return calc_thousands(coerced_str, units, tens, hundreds, thousands) 

        case default:
            print("An integer must be entered? what happened here?")
            return


roman_numeral(1943)

