a = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16]
print a[1:8]
print a[1:8:2]
print a[:8:2]
print a[::-1] #iteration start from last
print a[10::-1] #iteration start from last
print a[5::-2] # start at 6 and go reverse 2 steps

s = 'Hello, everybody!'
print s[1:8:2]
print s[:8:2]
print s[::-1] #iteration start from last- reversing

'''
sliceObj = slice(1, 8)
print sliceObj
print a[sliceObj]
'''
#sorting
a = [3, 6, 8, 2, 78, 1, 23, 45, 9]

print sorted(a) #source unaffected
print a
print sorted(a, reverse=True)
a.sort() # source modified
print a
a.sort(reverse=True) # source modified
print a


def getKey(item):
    return item[0]
def getValue(item):
    return item[1]

l = [[2, 3], [6, 7], [3, 34], [24, 64], [1, 43]]
print sorted(l,key=getKey)
print sorted(l,key=getValue)
