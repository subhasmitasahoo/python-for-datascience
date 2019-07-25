#dictionary
#.................................................................
    #curly brackets, (key, value) pairs

d = {'name':'subha', 'age':22}
print(d['name'])

d1 = {'letters':['a','b','c'], 'numbers':[1,2,3]}
print(d1['letters'][1])

#nested dictionary
#...................................................................
d2 = {'letters':{'capital':['A','B','C'], 'small':['a','b','c']}}
print(d2['letters']['capital'])

#tuple
#.................................................................
    # moon brackets
    #similar to list
    #these are immutable, values can't be reassigned

t = (0,1,2,3)
print(t[0])
# t[0] = 1 - gives error

#sets
#.................................................................
    #curly brackets
    #have unique values
    #similar to dictionary
s = {0,0,1,1,1}
print(s)
s.add(5)
print(s)

#comparison operators and if-else
#.................................................................
    # returns boolean value
    # logical operators - and, or

if(1>2):
    print('start')
elif(3==3):
    print('middle')
else:
    print('end')