print(2*2)

#1
print(2//2)


#1.0
print(2/2)

#when both ** arguments are integers, the result is an integer, too;
#when at least one ** argument is a float, the result is a float, too.


print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)




#The result produced by the division operator is always a float, 
# regardless of whether or not the result seems to be a float at first glance: 1 / 2, or if it looks like a pure integer: 2 / 1.

#division gives only float

print(6 / 3)    #-->2.0
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

#

print(6 // 3)    #gives integer---> 2
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
print()
print(-6 // 4)
print(6. // -4)


#   14 // 4 gives 3 → this is the integer quotient;
#   3 * 4 gives 12 → as a result of quotient and divisor multiplication;
#   14 - 12 gives 2 → this is the remainder.

print(14 % 4)



print(9 % 6 % 2)    #left Binding

#left Binding

#Right side Binding
# the exponentiation operator uses right-sided binding.
#256

print(2 ** 2 ** 3)

