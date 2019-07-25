# Q1. What is 7 to the power 4?
print(7**4)

# Q2. Split the String into a list
s = 'Hi there Sam!'
print(s.split()) 

# Q3 . print 'The Diameter of Earth is 12742 kilometers' using .format()
planet = 'Earth'
diameter = 12742
print('The Diameter of {planet} is {diameter} kilometers'.format(planet=planet, diameter=diameter))

# Q4. Given this nested list, use indexing to grab the word "hello"
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

# Q5. Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

# Q6. What is the main difference between a tuple and a list? 
# Ans. Tuple is immutable.

# Q7. Create a function that grabs the email website domain from a string in the form: user@domain.com
# So for example, passing "user@domain.com" would return: domain.com
s = 'user@domain.com'
print(s.split('@')[1])

# Q8. Create a basic function that returns True if the word 'dog' is contained in the input string. 
# Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization
# findDog('Is there a dog here?') -> True
# Additional: ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
s = 'Is there a dog here?'
print('dog' in s.lower().split())

count = 0
for w in s.lower().split():
    if(w == 'dog'):
        count += 1

print(count)


# Q9. Use lambda expressions and the filter() function to filter out words from a list 
# that don't start with the letter 's'. 
# For example: seq = ['soup','dog','salad','cat','great']
# should be filtered down to: ['soup','salad']
seq = ['soup','dog','salad','cat','great']
print(list(filter(lambda w: w[0] == 's', seq)))

# Q10. You are driving a little too fast, and a police officer stops you. 
# Write a function to return one of 3 possible results: 
# "No ticket", "Small ticket", or "Big Ticket". 
# If your speed is 60 or less, the result is "No Ticket". 
# If speed is between 61 and 80 inclusive, the result is "Small Ticket". 
# If speed is 81 or more, the result is "Big Ticket". 
# Unless it is your birthday (encoded as a boolean value in the parameters of the function) 
# -- on your birthday, your speed can be 5 higher in all cases.
# caught_speeding(81,True) -> 'Small Ticket'
# caught_speeding(81,False) -> 'Big Ticket'
def caught_speeding(speed, isBday):
    if isBday:
        speed -= 5
    if speed <= 60:
        return "No Ticket"
    elif speed <= 80:
        return "Small Ticket"
    return "Big Ticket"

print(caught_speeding(81, True))
print(caught_speeding(81, False))


