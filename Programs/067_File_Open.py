# File
f = open("emp.txt", "r")

for i in f:
    print(i)
    empno, name, salary = i.split(",")
    print(empno)
    print(name)
    print(salary)

