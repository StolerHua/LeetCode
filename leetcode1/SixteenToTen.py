while True:
    try:
        sixteen = raw_input()
        print int(sixteen, 16)
    except EOFError:
        break
