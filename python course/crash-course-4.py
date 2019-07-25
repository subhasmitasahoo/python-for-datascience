#MAP()
#.................................................................
def times2(n):
    return n*2
print(list(map(times2, [1,2,3,4,5])))

#LAMBDA EXPRESSION
#.................................................................
t = lambda n:n*2 #syntax:- lambda <params>: <returnValue>
print(t(2))

print(list(map(lambda n:n*2, [1,2,3,4,5])))

#FILTER FUNCTION
#.................................................................
filtered = list(filter(lambda n:n%2==0, [1,2,3,4,5])) #based on True or False, values are filtered
print(filtered)

#METHODS
#.................................................................
s = 'hello, I am subha'
print(s.capitalize())
print(s)
print(s.split())
print(s.split(','))

d = {'k1':1, 'k2':2}
print(d.keys())

l = [1,2,3]
print(l.pop())
print(l)
print(l.pop(0))
print(l)

l = [1,2,3,4,5]
print(1 in l)

x = [(1,2),(3,4),(5,6)]
for (a,b) in x:
    print('{} + {}'.format(a,b))
