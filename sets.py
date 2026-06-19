set1={1,2,3,4,5}
set2={3,4,5}
print(set1)
print(set2)
set3={ }
#print(set.__sizeof__(set3))
set1.add(10)
print(set1)
print(set1.difference(set2))
print(set1.difference_update(set2))
set1.intersection(set2)
print(set1)
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.pop())
set1.remove(10)
print(set1)