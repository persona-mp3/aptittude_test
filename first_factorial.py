"""
Have a function take the number parameter been passed and return the factorial of it. For example if:
num = 4, the function should return (4 * 3 * 2 * 1) = 24
"""

def first_factorial(num):
    INVALID_ARG = "Invalid arguments passed in, must be of type integer\n"
    INVALID_RANGE = "Invalid range passed in, must be of between 1 and 18\n"

    if type(num) != int:
        print(INVALID_ARG)
        return INVALID_ARG
    
    if num < 1 or num > 18:
        print(INVALID_RANGE)
        return INVALID_RANGE

    formatted_factorial = f""
    total = 1

    # range (start, stop, step) for countdown sequence, starts at 5, stops at 1, iterates seq by -1
    for x in range(num, 0, -1):
        # remove the extra * at the end of factorial reprsentation
        if x == 1:
            formatted_factorial += f"{x} "
            break

        formatted_factorial += f" {x} * "
        total *= x

    
    result = f"({formatted_factorial}) = {total}\n"
    print(result)
    return result

first_factorial(5)
first_factorial(18)
first_factorial(20)
first_factorial(11)

