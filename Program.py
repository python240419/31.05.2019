
print('Hello World!')

# this does not run!
'''
this will not run
multi-line
'''
# staring with 5 numbers
#userInput = input("Please insert a number:");
#print(type(userInput))

x = input("Please insert 1st number:");
x = float(x)

y = float(input("Please insert 2nd number:"));

print("{} + {} = {}".format(x, y, x + y));
print("{} - {} = {}".format(x, y, x - y));
print("{} * {} = {}".format(x, y, x * y));
print("{} / {} = {:.2f}".format(x, y, x / y));
print("{} // {} = {}".format(x, y, x // y));
print("{} ** {} = {}".format(x, y, x ** y));
print("{} \u221A {} = {}".format(x, y, x ** (1/y)));
print("{} % {} = {}".format(x, y, x % y));

# go down a line using \
print("go down a line .... {}".\
      format(3))


fullName = input("Enter you full name:")
lst = fullName.split()
fname = lst[0] # item in the first index
lname = lst[1] # item in the second index
print("Your name is Mr.{}, {}".format(lname, fname))

# Optional shortcut: fname = fullName.split()[0];
# Optional shortcut: fname = fullName.split()[0];
# print("Your name is Mr.{}, {}".format(fullName.split()[1], fullName.split()[0]))

formula = input("Enter calculation , format: X + Y:")
lst = formula.split()
x = float(lst[0])
y = float(lst[2])
oper = lst[1]
z = x + y
print("{} + {} = {}".format(x, y , z))

# if-else ...
age = int(input("Enter your age:"))
# > < == >= <=
if age >= 18:
    print("{} is bigger equal than 18".format(age))
else:
    print("{} is lower than 18".format(age))

print("after if")
#age = 7
if age <= 3:
    print("you are a baby")
elif age <= 12:
    print("you are a child")
elif age <= 18:
    print("you are a teenager")
else:
    print("you are a grown-up")
   
# outside the if    

formula = input("Enter calculation , format: X + Y:")
lst = formula.split()
oper = lst[1];
x = float(lst[0])
y = float(lst[2])

if oper in ["+", "-", "/", "*"]:
    print("{} is legal operator".format(oper))
    if oper == "+":
        print("{} + {} = {}".format(x, y, x + y))
    elif oper == "-":
        print("{} - {} = {}".format(x, y, x - y))
    elif oper == "*":
        print("{} * {} = {}".format(x, y, x * y))
    elif oper == "/":
        print("{} / {} = {}".format(x, y, x / y))
else:
    print("{} is an illegal operator".format(lst[1]))

age = int(input("Enter your age:"))

if age >= 20 and age <= 25 or age <= 0:
    print("{} is between 20-25 or its negative".format(age))

    #if oper == "+" or oper == "-" or oper == "/" or oper == "*":
    #if oper in ["+", "-", "/", "*"]:

# split - delimiter
# list
# if elif else and or == != > < >= <=
# in
# eval

# input formula from user
# 3+5
# 3 + 5
# check if delimiter is " " -- print the result




