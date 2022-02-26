decls = ['процент', 'процента', 'процентов']

percents = int(input("Input percents: "))

"""Get remainder"""
last_digits = percents % 100

"""Handle numbers above 20 due to russian language declination application rules"""
if last_digits > 20:
    last_digits = last_digits % 10

"""Print response"""
if int(last_digits) >= 5:
    print(str(percents) + "% " + decls[2])
elif int(last_digits) > 1:
    print(str(percents) + "% " + decls[1])
else:
    print(str(percents) + "% " + decls[0])
