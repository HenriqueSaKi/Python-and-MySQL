#list comprehension

x = [1, 2, 3, 4, 5]
y = [] 

#Beginner way to add all values into 'y' after transformation
for i in x:
    y.append(i**2)
print(y)

print ("-----------------------------")

#Advanced way to make the same operation
y = [i**2 for i in x]
print(y)

print ("-----------------------------")

#Advanced way to filter just odd values
z = [i for i in x if i%2==1]
print(z)