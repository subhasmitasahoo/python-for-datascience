#FOR LOOP
#.................................................................
seq = [1,2,3,4,5]

for num in seq:
    print(num)


#WHILE LOOP
#....................................................................

i = 1
while i < 10:
    print('i is {}'.format(i))
    i+=1

#RANGE FUNCTION
#.................................................................

for x in range(0,10):
    print(x)

print(list(range(0,10)))

#LIST COMPREHENSION
#.................................................................

#What does it to do?
list1 = [1,2,3,4,5]
list2 = []
for num in list1:
    list2.append(num**2)
print(list1)
print(list2)

#list comprehension equivalent
list3 = [num**2 for num in list1]
print(list3)


#FUNCTION
#.................................................................
print('.....function.....')
def func1(x=5):
    for i in range(x):
        print(i)

func1(10)
func1() #takes the default value as param

def square(num):
    """
    This is a square function which returns the square of a number
    """
    return num**2

print('output is {}'.format(square(3)))
