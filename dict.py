# encoding: utf-8

d1 = dict()
d1['Name'] = "John"
d1['Address'] = "XXXY"

d2 = {"Name": "John", "Address": "XXX"}

d3 = {}.fromkeys(["Name", "Address", "Phone"], "N/A")

d = {"Name": "John", "Address": "XXX"}
name = d["Name"]
# name is John

d = {"Name": "John", "Address": "XXX"}
name = d.get("Name")
Id = d.get("ID")
Id = d.get("ID", "Not There!")
# name is John and Id is None and Id is Not There!

d = {"Name": "John", "Address": "XXX"}
d['Name'] = "Salt"
# name is Salt!

d = {"Name": "John", "Address": "XXX"}
d.setdefault("phone", "1235")
# phone is 1235!

d = {"Name": "John", "Address": "XXX"}
d.update({"phone": "12344", "City":"Berlin"})
# Now d also has a City and Phone!


d = {"Name": "John", "Address": "XXX"}
for key in d.keys():
    print(key)
# Ouput: Name, Address

d = {"Name": "John", "Address": "XXX"}
for val in d.values():
    print(val)
# Ouput: John, XXX


d = {"Name": "John", "Address": "XXX"}
for key, val in d.items():
    print(key + ":" + val)
# Ouput: Name:John,  Address:XXX


d = {"a": 2, "b":-1, "c": 0}
print(sorted(d))
# output: ['a', 'b', 'c']

import operator
d = {"a": 2, "b":-1, "c": 0}
s_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
# Output:  {'b': -1, 'c': 0, 'a': 2} 
