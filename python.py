def reverse(a,r):
    for i in range(len(str(a))):
        r=a[::-1]
        if (r==a):
            return "it is a"
        else:
            return "it is not a"
    reverse(a,r)


a="racecar"
r=""
