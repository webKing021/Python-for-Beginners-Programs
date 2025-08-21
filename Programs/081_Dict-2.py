nd = {1:{"name":"krutarth", "roll":21}, 2:{"name":"het", "roll":63}}
nd[1]["name"]
nd[1]["roll"]
nd[2]["name"]

# add new dict
nd[3] = {}
nd[3]["name"] = "superman"
nd[3]["roll"] = 05

nd[4] = {"name":"spiderman", "roll":06}

# del
del nd[4]
del nd[3]["roll"]

# iterate
for key, r in nd.items():
    print("key : " , key)
    print("value : " , r)

for key in r:
    print(key + " : " + r[key])

# Example - 1 : salary slip

people = {1:{"name":"krutarth", "basic":20000, "sex":"male"}, \
2:{"name":"het", "basic":25000, "sex":"male"}, \
3:{"name":"maria", "basic":22000, "sex":"female", "married":"no"}, \
4:{"name":"raj", "basic":24000, "sex":"male", "married":"yes"}}

for k, v in people.items():
    name = v["name"]
    basic = int(v["basic"])
    hra = basic * 50/100
    da = basic * 20/100
    allow = 800
    gsal = basic + hra + da + allow
    print("*********** Salary Slip ***********")
    print("Name : " + name)
    print("Basic : " + basic)
    print("hra", hra, " da : ", da, " allow : ", allow)
    print("Gross Salary : ", gsal)
    print("*********** End ***********")

# Example - 2 : 
d1 = {1:"het",2:"krutarth,3:"superman",4:"spiderman"}
d2 = {}

for k,v in d1.items():
    if v not in d1.values():
        d2[k] = v

print(d2)


# Example - 3 : 
emp = {1:("het",25000), 2:("krutarth",26000), 3:("superman",27000), 4:("spiderman",28000)}
pid = int(input("Enter empid : "))
L = []
if pid in emp:
    name,salary = emp[pid]
    if L[1] > salary:
        emp[pid] = (name,salary + 500)
print(emp)
    