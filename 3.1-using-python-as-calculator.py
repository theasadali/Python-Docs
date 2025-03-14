# comments start with # symbol
# starting with operators and numbers

print(2+2) # add operands
print(2-4) # subtracts right operand from left operand
print(34*4) # multiply the operands
print(4/3) # divides the left operand by right operand
print(6//4) # floor operator divides the number and returns the intergral part of number
print(50 - 6 * 8) # (*) operator has higher precedence
print(45 % 3) # remainer operator return remainder after division
print(31**2) # power operator 


# = operator is used to assign values to variables
a = 2 # type <class 'int'>
b = 4.7 # <class 'float'>
c = 'a' # <class 'str'>
d = 'Hello World!' # <class 'str'>

#3.1.2 TEXTS
#string concatenation
str1 = "py"
print(str1 + "thon")
#output: python

#indexing strings
mystr = "Hi There!"
print(mystr[0])
#output: H

print(mystr[1:])
#output: i There!

#negative indexing - starts from -1 from right to left unlike 0 from left to right
print(mystr[-2])
#output: e

print(mystr[1:5]) # Hi There!
#ouput: i Th | first index included - last index not included in ouput

print(mystr[-2:-1]) 
#output: e | first index included - last index not included in ouput

print(mystr[-2:])
#output: e! | first index included - last index not included in ouput

#s[:i] + s[i:] is always equal to s
print(mystr[:2] + mystr[2:])
#output: Hi There!

