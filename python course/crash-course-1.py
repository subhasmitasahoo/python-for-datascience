#arithmetic - integer, float
    #integer division can return float

#To print
print('Hello World!')

#Print formatting
print('hello, my name is {} and I am {}'.format('subha', 22))
print('hello, my name is {name} and I am {age}'.format(name='subha', age=22))

#strings
s1 = 'python course'
print(s1[3:])
print(s1[:2])
print(s1[3:10])

#list
letters = ['a','b','c']
print(letters)
letters.append('d')
print(letters)
letters.append(2)
print(letters)
print(letters[1:])
letters[4] = 'e'
print(letters)

#nested list
nestedLetters = [['a','b'],['c','d']]
print(nestedLetters)