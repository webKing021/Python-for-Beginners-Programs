lines = ['Readme','How to write text files in Python']
with open('readme.txt','w') as f:
    f.writelines(lines)

#File Exception Handling
try:
    f = open('event.txt',"r")
    #perform file operations
except FileNotFoundError:
    print("File Block error.")
finally:
    print("File Finally")
    f.close()
