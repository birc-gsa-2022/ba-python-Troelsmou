#import random

def border_array(x):
    border_array = [0]
    for i in range(1, len(x)):
        b = border_array[i - 1]
        while True:
            if read[b] == x[i]:
                border_array.append(b + 1)
                break
            elif b == 0:
                border_array.append(0)
                break
            else:
                b = border_array[b-1]
    return(border_array)

#def generate_string(seed_string, length):
#    string = ""
#    for j in range(length):
#            string += random.choice(seed_string)
#    return(string)

def strict_border_array(x):
    ba = border_array(x)
    for i in range(len(ba) - 1):
        if ba[i] == 0 or x[ba[i]] != x[i + 1]: #skips if border array is 0 or the characters after the borders don't match.
            continue
        else:
            while ba[i] != 0 and x[ba[i]] == x[i + 1]:
                ba[i] = ba[ba[i] - 1]
    return(ba)

#read = generate_string("abcdefghijklmnopqrstuvxyzæøå", 10**6)
#bax = strict_border_array(read)

#for i in range(len(bax) - 1):
#    if bax[i] == 0:
#        continue
#    assert read[0:bax[i]] == read[i - bax[i] + 1:i + 1], "is not a border"
#    assert read[bax[i]] != read[i + 1]

#    print(i, read[0:bax[i]], read[i - bax[i] + 1:i + 1], bax[i], read[bax[i]], read[i + 1])
#print(bax)