x = {"apple", "banana", "cherry"} 
y = {"google", "microsoft", "apple"} 
x.symmetric_difference_update(y) 
print(x) 
print(y)

# s1={12,34,5,6,78}
# s2={12,5,678,90}
# s3=s1.symmetric_difference(s2)
# print(s1)
# print(s2)
# print(s3)
s1={12,34,5,6,78}
s2={12,5,678,90}
s3=s1^s2  # bitwise x-or
print(s1)
print(s2)
print(s3)
