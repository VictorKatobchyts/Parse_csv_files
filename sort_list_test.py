x = 2, 2, 4, 3, 3, 1, 1, 2, 5, 4, 2, 1
print('data1:', x)
def unique(obj: iter):
    args = []
    for a in obj:
        if a not in args:
            args.append(a)
            yield a

r = unique(x)
print('original sort unique:', *r)