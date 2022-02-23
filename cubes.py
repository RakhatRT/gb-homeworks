digits = list()
response = 0

def split_number(number):
    number = list(str(number))  # convert into string to split by digits
    number = list(map(int, number))  # convert into int to allow arithmetics
    return number


def join_number(digits):
    digits = list(map(str, digits))  # convert into string for join
    digits = int(''.join(digits))  # convert digits into whole number
    return digits


def calc_digits_sum(digits):
    return sum(digits)


"""Fill list with values"""
for number in range(1,51,2):
    number = pow(number, 3)  # power into third
    digits.append(split_number(number))

print("Initial cubes list is ", digits)

""" Fill response with values which digits sum is exactly dividing by 7"""
for number in digits:
    digits_sum = calc_digits_sum(number)
    if digits_sum % 7 == 0:
        print(str(join_number(number)) + " = " + str(digits_sum))
        response += join_number(number)

print(f"response: {response}")

"""Reset response"""
response = 0


""" Fill response with (values + 17) which digits sum is exactly dividing by 7"""
for number in digits:
    number = join_number(number) + 17
    number = split_number(number)
    digits_sum = calc_digits_sum(number)
    if digits_sum % 7 == 0:
        print(str(join_number(number)) + " = " + str(digits_sum))
        response += join_number(number)

print(f"response: {response}")
