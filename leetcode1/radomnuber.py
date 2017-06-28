while True:
    try:
        num = []
        n = input()
        for i in range(n):
            num.append(input())
        sortNum = sorted(set(num))
        for num in sortNum:
            print num
    except EOFError:
        break

