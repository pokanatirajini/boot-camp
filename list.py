#list methods
for m in dir(tuple):
    if not m.startswith("__"):
        print(m)"""
#list
import sys
import copy
my_list=[None]*10
for i in range(10):
    my_list[i]=i
print(my_list)
print(sys.getsizeof(my_list))
print(list.__sizeof__(my_list))
s_list=my_list
s_list[4]=40
print(s_list)
print(my_list)
d_list=copy.deepcopy(my_list)
d_list[9]=50
print(d_list)
print(my_list)