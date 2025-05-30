# #Conditions 
# IF
#  if is used to check if a condition is true and to execute the block code.

 a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number



# If Else
# If condition is true the first block will be executed, if not the else condition will run.
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')



# If Elif Else
# In our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions but multiple conditions. 
# As similar to life, programming is also full of conditions. We use elif when we have multiple conditions.

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')


# Nested Conditions
# Conditions can be nested

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')


# If Condition and Logical Operators

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')


#If and Or Logical Operators

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')



