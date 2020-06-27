def addAndDouble(n):
    for i in range(0, n):
        nextNum = i + 1
        yield i, nextNum
        doubleNextNum = nextNum * 2
        yield i, doubleNextNum


count = 0
for num, xform in addAndDouble(10):
    if count %2 == 0:
        print("Adding 1 to {} makes {}. ".format(num, xform), end = '')
    else:
        print("Then doubling it makes {}".format(xform))
    count += 1