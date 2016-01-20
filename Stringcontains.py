s = "It's not safe to go alone. Take this."
print 'safe' in s
print 'blah' in s

#or

if s.find('safe') != -1:
    print('This message is safe.')