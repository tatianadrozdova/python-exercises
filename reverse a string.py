# input: I am Tanya I live in Santa Clara
# output: Clara Santa in live I Tanya am I

n = "I am Tanya I live in Santa Clara"

def reverse(n):

    n = n.split()
    r = []
    print(n, type(n))

    for i in range(-1, -len(n) - 1, - 1):
        r.append(n[i])
    print("r is %s" % r)

    r = " ".join(r)

    return r

print(reverse(n))



