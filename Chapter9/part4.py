fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1

# print(di)

#now we want to fid the most common word
largest = -1
theword = none
for k,v in di.items() :
    if v > largest :
        largest = v
        thrword = k #cature/remember the key that was largest

print(theword, largest)

