while True:
    try:
        n = input()
        if n:
            print n/2
        else:
            break
    except EOFError:
        break
