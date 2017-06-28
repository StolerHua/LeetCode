import re


def counts(s):
    # print re.findall('\d+', s)
    # print re.findall('[a-zA-Z]+', s)
    # print re.findall('\W+', s)
    return len(re.findall('[a-zA-Z]+', s)), len(re.findall('\d+', s)), len(re.findall('\W+', s))

while True:
    try:
        inputs = raw_input().split(' ')
        count1 = count2 = count3 = 0
        for s in inputs:
            count1 += counts(s)[0]
            count2 += counts(s)[1]
            count3 += counts(s)[2]
        print str(count1) + ',' + str(count2) + ',' + str(count3)
    except EOFError:
        break
#
# print counts("abcd1244!!12cd")