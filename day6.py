#LOOPS

# While Loop
# We use the reserved word while to make a while loop. It is used to execute a block of statements repeatedly until a given condition is satisfied. 
# When the condition becomes false, the lines of code after the loop will be continued to be executed.


count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4

#Break
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

#Continue
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1



#Loop in sets 

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# For Loop
# A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences.
#  Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out


#NESTED LOOPS - we can write a loop inside a loop
# syntax
for x in y:
    for t in x:
        print(t)

        

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
