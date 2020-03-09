d = {'test': 1, 'TEST2': 2}

print(d)

c = dict(short='dict', longer='dictionary')

print(c)

d['short'] = 'hahaha'
print(d)

r = dict.fromkeys(['a', 'b'], 2)
print(r)

a = 'eee'
print(r)

ttt = {g: g * 2 for g in range(7)}
print(ttt)

person = {
    'name': {'last_name': 'Иванов', 'first_name': 'Иван'},
    'address': ['г. Москва',
                "ул. Садовая д. 12",
                "кв. 77"],
    "phone": {'home_phone': "99-99-99",
              'work_phone': "88-88-88",
              'mobile_phone': "55-55-55"},
    'key': 'value_of_key'
}
print("_____________")
print(person)
print("print(person.values()):")
print(person.values())
print("print(person.keys()):")

print(person.keys())
print("print(person.popitem())")
print(person.popitem())
print("print(person)")
print(person)
print('print(person.update(key345=3))')


person2 = person.copy()
print("print(person2)")
print(person2)