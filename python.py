
my_dict = {'key1': 'value1',
'key2': 'value2',
'key3': 'value3'
}

grocer1 = {'fruit':'apple', 'drink':'water'}
grocer2 = dict(fruit='apple', drink='water')
print(grocer1)
print (grocer2)

sozluk = {'ali':25, 'veli':30, 'ayse':35}
type(sozluk)

# The key should be unique and an immutable object.

print(type (sozluk))

state_capitals = {'Arkansas': 'Little Rock',
'Colorado': 'Denver',
'California': 'Sacramento',
'Georgia': 'Atlanta'
}
print(state_capitals ['Colorado']) # accessing method

sozluk = {'ali':25, 'veli':30, 'ayse':35, 'ali':40}

sozluk = {'ali': 'mehmet', 'veli': 'ahmet', 'ayse': 'fatma'}

sozluk = {'ali': [30,4,68], 'veli': (2,3,4), 'ayse': True}

sozluk = {5: 'mehmet', 7: 'ahmet', 9: 'fatma'}

sozluk = {(1,2,3): 'mehmet', 7: 'ahmet', 9: 'fatma'}

text = 'abcde'
type(text)

liste = [1,2,3,4]
liste[2] = 95

dict(ali = 25, mehmet = 30, fatma = 35)

dict([('ali', 25), ('mehmet', 30), ('fatma', 35)])

dict(ali = (25,30,35,40), mehmet = 30, fatma = 35)

text.replace('cd', 'klm')

state_capitals = {'Arkansas': 'Little Rock',
'Colorado': 'Denver',
'California': 'Sacramento',
'Georgia': 'Atlanta'
}
state_capitals [ 'Virginia'] = 'Richmond' # adding a new item
print(state_capitals)

sozluk = {'ali':25, 'veli':30, 'ayse':35}
sozluk ['ali']
sozluk ['ayse']
sozluk ['mahmut'] = 55

mix_values = {'animal': ('dog', 'cat'), # tuple type
'planet': ['Neptun', 'Saturn', 'Jupiter'], # list type
'number': 40, #int type
'pi': 3.14, # float type
'is_good': True} # #bool type

mix_keys = {22 : "integer",
1.2 : "float",
True : "boolean",
"key": "string"}

sozluk['veli']
sozluk [ 'veli'] = 25
sozluk.get('ali')
sozluk.get('hasan')

sozluk.get('hasan', 'Kardesim duzgun yaz, Oyle bir key degeri yok')

family = {'name1': 'Joseph',
'name2': 'Bella',
'name3': 'Aisha'
}

sozluk ['hasan'] = 77

family['name4'] = 'Tom'
print(family)

dict_by_dict = dict(animal='dog', planet='neptun', number=40, pi=3.14, is_good=True)
print(dict_by_dict)

family = dict(name1 = 'Joseph', name2 = 'Bella', name3 = 'Aisha',
name4 = 'Tom')
print(family)

dict([('namel', 'ali'), ('name2', 'ayse'), ('name3', 'fatma')])

dict([('namel', 'ali'), ('name2', 'ayse'), ('name3', 'fatma'), ('namel', 'kahraman')])

sozluk.items()
sozluk.keys()
type(sozluk.keys())

keyler = list (sozluk.keys())
sozluk.values()

dict_by_dict = {'animal': 'dog',
'planet': 'neptun',
'number': 40,
'pi': 3.14,
'is_good': True}
print(dict_by_dict.items(), '\n')
print(dict_by_dict.keys(), '\n')
print(dict_by_dict.values())

print(list(family.items()), "\n")
print(list(family.keys()), "\n")
print(list(family.values()))

dict_by_dict = {'animal': 'dog',
'planet': 'neptun',
'number': 40,
'pi': 3.14,
'is_good': True}
dict_by_dict.update({'is_bad': False})
print(dict_by_dict)

sozluk.update({'kemal':21})
sozluk [ 'huseyin'] = 27

family = {'name1': 'Joseph',
'name2': 'Bella',
'name3': 'Aisha',
'name4': 'Tom'
}
family.update({'name5': 'Alfred'})
print (family)

dict_by_dict = {'animal': 'dog',
'planet': 'neptun',
'number': 40,
'pi': 3.14,
'is_good': True,
'is_bad': False}
del dict_by_dict['animal']
print(dict_by_dict)

kelime = 'abcdefg'
listem = list (kelime)
del listem [2]

del sozluk ['hasan'] 

help('keywords')

sozluk ['mahmut'] = None

sozluk ['mahmut'] = [25,76]

sozluk ['mahmut']
sozluk ['mahmut'] [1]
sozluk ['mahmut'] [1] = 45
del sozluk ['mahmut'] [1]
del sozluk

del family['name2']
del family['name3']
print(family)

sozluk = {'ali': 25, 'veli': 25, 'ayse': 35, 'mahmut': [25], 'kemal': 21, 'huseyin': 27}
liste.pop()
liste.pop(0)
sozluk.pop('mahmut')

sozluk.pop('mahmut', 'Bulamadim kiiii Sileyim')

sozluk.popitem()

List = {"item1", "item2", "item3" "item4" } #A
List = ("item1", "item2" "item3", "item4") #B
List = ["item1", "item2", "item3", "item4"] #C
List = ["item1", "item2", "item3", "item4"] #D

city = ['Los Angeles', 'Beirut', 'Tokyo']
city [1] = 'Istanbul'
print(city)

a = [1,2,3,4,5]
del a[2]

a = [1,2,3,4,5]
a.remove(3)

a = [1,2,3,4,5]
a [2:3] = [ ]
print(a)

a = [1,2,3,4,5]
a[2:4] = ['a', 'b', 'c', 'd']

5 in a
7 in a
2 not in a
8 not in a
'ali' in sozluk
21 in sozluk
'ayse' not in sozluk
21 in sozluk.values()
('ali',25) in sozluk
('ali',25) in sozluk.items()

dict_by_dict = {'planet': 'neptun',
'number': 40,
'pi': 3.14,
'is_good': True,
'is_bad': False}
print('pi' in dict_by_dict) 
print('animal' not in dict_by_dict) # remember, we have deleted 'animal'
print('pi'in dict_by_dict)

print('name3' in family)

school_records={
"personal_info":
{
    "kid":{"tom": {"class": "intermediate", "age": 10},
        "sue": {"class": "elementary", "age": 8}
},

"teen":{"joseph": {"class": "college", "age": 19},
"marry":{"class": "high school", "age": 16}
},
},
"grades_info":
{"kid":{"tom": {"math": 88, "speech": 69},
"sue": {"math": 90, "speech": 81}
},
"teen":{"joseph": {"coding": 80, "math": 89},
"marry":{"coding": 70, "math": 96}
},
},}
print(school_records ['grades_info'])
print(school_records ['grades_info']['teen'])
print(school_records [ 'grades_info']['teen'] ['joseph'])
print (list (school_records ['grades_info']['teen' ] [ 'joseph'].items()))

school_records={
"personal_info":
{"kid":{"tom": {"class":"intermediate", "age":10},
"sue": {"class": "elementary", "age":8}
},
"teen":{"joseph": {"class": "college", "age":19},
"marry":{"class": "high school", "age": 16}
},
},
}
print(school_records['personal_info'])
print(school_records['personal_info']['teen'])
print(school_records['personal_info'] ['teen']['marry'])
print(school_records['personal_info']['teen'] ['marry'] ['age'])

friends = {
"friend1":{"first" : "Sue", "last" : "Bold"},
"friend2":{"first" : "Steve", "last" : "Smith"},
"friend3":{"first" : "Sergio", "last": "Tatoo"}
}
print (friends)

favourite = {
"friends" : {
"friend1": {"first" : "Sue", "last" : "Bold"},
"friend2":{"first" : "Steve", "last" : "Smith"},
"friend3":{"first" : "Sergio", "last": "Tatoo"}
},
"family" : {
"family1" : {"first" : "Mary", "last": "Tisa"},
"family2":{"first" : "Samuel", "last": "Brown"},
"family3": {"first": "Tom", "last" : "Happy"}
}
}
print (favourite)