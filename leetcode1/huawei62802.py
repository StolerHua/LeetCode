def ReverseWords(s):
    temp = s.split(' ')
    outputs = []
    for t in temp:
        if t is not '':
            outputs.append(t)
    outputs = outputs[::-1]
    s = ' '.join(outputs)
    return s

print ReverseWords("sdasad\n")