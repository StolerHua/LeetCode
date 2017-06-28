import re
inputs = "(search (combine \"1234567890\" \"abcdefgh\" \"1234567890\") (reverse \"#####\"))"
# s = "(search \"huawei\" \"we\")"

def simple(s):
    orders = re.findall('[\w]+', s)
    order = orders[0]
    if order == "search":
        index = orders[1].find(orders[2])
        if index == -1:
            return ""
        else:
            return orders[1][index:]
    if order == "quote ":
        return orders[1]
    if order == "reverse":
        return orders[1][::-1]
    if order == "combine":
        st = ""
        for pa in orders:
            if pa != "combine":
                st += pa
        return st


def multi(inputs):
    orders = re.findall('(?<=[\(])[^\)\(]+(?=[\)])', inputs)
    while orders != []:
        for order in orders:
            result = simple(order)
            order = '(' + order + ')'
            inputs = inputs.replace(order, result)
        orders = re.findall('(?<=[\(])[^\)\(]+(?=[\)])', inputs)
    print '"'+inputs+'"'

# while True:
#     try:
#         inputs = raw_input()
#         multi(inputs)
#     except EOFError:
#         break
multi(inputs)