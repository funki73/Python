# def multiply(num_list, num):
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # output:
# >>>[2,4,10,16]

# def multiply(num_list, num): #don't go inside the function until the function is called
#     a = [2,4,10,16]
#     b = multiply(a,5) # now our function executes; what is a function call equal to?
# print(b) # and the resulting value is printed

# def multiply(num_list, num):
#     print(num_list, num)
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # output:
# # >>>[2,4,10,16] 5
# # >>>[2,4,10,16]

def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[10,20,50,80]




