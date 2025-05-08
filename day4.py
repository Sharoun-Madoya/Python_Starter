#DICTIONARY
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
# To create a dictionary we use curly brackets, {} or the dict() built-in function.


# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4


person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'skills': ['python','java','flask', 'databases'],
   'city':'Helsinki',
   'address':{
        'street':'Mombasa',
        'postcode':'01-0098-8354'
   }
   }

print(person_info.get('firstname')) # Asabeneh
print(person_info.get('country'))    # Finland
print(person_info.get('skills'))     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person_info.get('skills'[0]))  # JavaScript
print(person_info.get('address','street')) # Space street
print(person_info.get('city'))       # Error
person['first_name'] = 'Eyob'
person['age'] = 252


# person['job_title'] = 'Instructor'
# person['skills'].append('HTML')
# print(person)


# Adding Items to a Dictionary
# We can add new key and value pairs to a dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'

dct.pop('key1') # removes key1 item
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
dct_copy = dct.copy()
keys = dct.keys()
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])