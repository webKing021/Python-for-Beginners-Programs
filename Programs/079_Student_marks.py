#  WAP to create a student.txt and add few student's name with 3 subjects marks then read the file and check if student has less 
# than 40 marks in any then print failed, else print pass.
f = open("student.txt", "r")
for i in f:
    print(i)
    m = i.split(",")
    if int(m[1]) < 40 or int(m[2]) < 40 or int(m[3]) < 40:
        print("Failed")
    else:
        print("Pass")
f.close()
