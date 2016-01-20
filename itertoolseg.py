import itertools

horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(list(itertools.permutations(horses)))
print(list(itertools.combinations(horses,4)))


letters = ['a', 'b', 'c', 'd', 'e', 'f']
booleans = [1, 0, 1, 0, 0, 1]
numbers = [23, 20, 44, 32, 7, 12]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]

mylist =  list(itertools.chain(letters, booleans, decimals))

print mylist

#compress
print list(itertools.compress(mylist, [1,1,0,1]))

import time
print time.gmtime()
current_time = time.localtime()
print time.strftime('%Y-%m-%d %A', current_time)