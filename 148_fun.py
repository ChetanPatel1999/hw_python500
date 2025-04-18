#The lambda /Anonymous Functions
add=lambda a,b :a+b
square=lambda num : num*num
cube= lambda num : num*num*num
average = lambda a,b: (a+b)/2
greater = lambda a,b: a if a>b else b
greater_three = lambda a,b,c: a if a>b and a>c else b if b>c else c

fun=lambda :print("lambda")

fun2 = lambda a,b :print("great : ",a) if a>b else print("great : ",b) 

greater_four = lambda a,b,c,d: a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d
print("sum : ",add(12,8))
print("square of 5 :" ,square(5))
print("cube of 4 :" ,cube(4))
print("avrage  of 4 and 5.5 :" ,average(4,5.5))
print("greatest num : ",greater(34,56))
print("greatest num : ",greater_three(34,123,67))
fun()
fun2(344,222)
print(greater_four(34,5666,78,900))