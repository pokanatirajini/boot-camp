#list

list1=[]
for i in range(5):
    element=int(input())
    list1.append(element)
print(list1)
print(tuple2[-2])
print(tuple2[1:3])
list1.remove(30)
print(list1)
print(list1.pop())
list1.insert(2,90)
print(list1)

#tuple

tuple1=(10,20,30,40,50,'hi')
print(tuple1)
tuple2=(1,2,3,4,5)
print(tuple2)
print(tuple2[3])
print(tuple2[-2])
print(tuple2[1:3])
print(tuple1+tuple2)
print(tuple1*3)
print(20 in tuple1)
print(90 not in tuple1)
print(len(tuple1))
print(tuple1.count(2))

#set

a={1,2,3,4}
b={'a','b','c','d'}
print(a)
print(b)
print(a&b)
print(a|b)
print(a-b)
print(a^b)   #symmetric differ
print(20 in a)
print(90 not in b)
print(len(a))"""

#dictionaries

dic={'name':'rajini','roll':26}
print(dic)

