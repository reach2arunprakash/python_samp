# coding=utf-8
#S = {x² : x in {0 ... 9}} ==> 0 1 4 9 ....81
#V = (1, 2, 4, 8, ..., 2¹²)
#M = {x | x in S and x even}
'''[output_expression looping_variable optional_predicate]'''

a = [x**2 for x in range(10)]
v= [2**x for x in range(0,12)]
m = [x for x in a if x%2==0]
print a
print v
print m


words = 'The quick brown fox jumps over the lazy dog'.split()
reverall = [w[::-1] for w in words]
rever = [w[::-1] for w in words if w.startswith('o')]

print words
print rever
print reverall


'''
mygenerator = (x*x for x in range(3)) ---> () instead of []
for i in mygenerator:
    print "first"
    print(i)

for i in mygenerator:
    print "second"
    print(i)

'''



#Yield is a keyword that is used like return, except the function will return a generator.

'''