# empty dictionary
d = {}
d

# with datatype 
d = {1: 1, 2: 2, 3: 3}
d

d = {1: "Krutarth", 2: "Python", 3: "Programming"}
d

# mix datatype
d = {1: "Krutarth", 2: 21, 3: 9.27, 4: [2,3,4]}
d
d[1][2]
d

# with dict() function
d = dict({1: 21})
d

d = dict([{1, "apple"}, {2, "banana"}])
d

# dict() with tuple
d = dict([(1, "apple"), (2, "banana")])
d

# 
d = {1:"apple",2:["a","b","c"], 3:(1,2,3)}
d
d[1]
d[2]
d[3]

# try to print inner value
d = {1: [2,3,4,5]}
d[1][1]
d[1]

# keys()
d.keys()

# values()
d.values()

# items()
d.items()

# type()
type(d)

d[0]:1234
d[1] = 21

d1 = {"name": "Krutarth", "roll": 21}
d1.keys()
d1["roll"]
d1
d1.get("name")
d1

# nested
d = {"d":{1:"ljku"}, "e":{"name":"Krutarth"}}
d["1"]
d["e"]["name"]
d["d"]

d3 = {1:1, 2:8, 3:27, 4:64}
d3[1]
d3[2]
d3[3]
d3[4]

# for loop
for i in d3:
    print(d3[i])

for i in d3.keys():
    print(i)

for i in d3.values():
    print(i)

for i in d3.items():
    print(i)

d = {}
for i in range(4):
    d[i] = i*i*i
d

# del
del d3[1]
d3

# dict built-in functions
d = {1:1, 2:2, 3:3, 4:4}
print(any(d))
print(all(d))
print(len(d))
print(sorted(d))
print(sum(d))
print(max(d))
print(min(d))
d.clear()
d.update()
d.pop(1)
b = d.copy()
b

# update
d1 = {"name": "Krutarth", "roll": 21, "age":20}
d2 = {"name": "Krutarth", "roll": 21}
d1.update(d2)
d1

# pop
d1.pop("name")
d1
d.values()
d

# popitem()
d.popitem()
d

# has_key()
d.has_key("name")
d

# setdefault()
d.setdefault("name", "Krutarth")
d

# curd
d["address"] = "Delhi"
d

# comprehension
d = {i:i*i for i in range(11) if i%2==1}
d

# membership
"name" in d
"Krutarth" in d.values()
"Krutarth" not in d.values()

# list comprehension
l = {word: len(word) for word in ["Krutarth", "Raychura"]}
l

d = {}
s = input("Enter a string: ")
for i in s:
    if (i in d.keys()):
        d[i] = int(d[i]) + 1
    else:
        d[i] = 1
d






