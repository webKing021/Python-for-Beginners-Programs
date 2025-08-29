# Call by Value vs Call by Reference

def modify_int(a):
    a += 10
    return a

def modify_list(lst):
    lst.append(99)
    return lst

nums = [1, 2, 3]
print("Before modify_list, nums =", nums)
modify_list(nums)
print("After modify_list, nums =", nums)
