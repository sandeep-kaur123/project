t =("sandeep","MCA","oct4")
print(t)
fish=(1,2,"red","blue")
print(fish[0])
#fish[0] = 7     #we cannot change the elements in tuple bcz it is immutable

print(len(fish))
print(fish[:2])
print("red" in fish)

t1= 12345,54321,'hello!' #comma separator value return tuple
print(t1)
print(type(t1))
x,y,z = t1
print(x) #unpacking
print(y)
print(z)

x=10
y=9
x=x^y #swapping using xor
y=x^y
x=x^y
print(x)
print(y)

x,y = y,x
print(x,  y) #tupple packing
