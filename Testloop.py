def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i

a = [1,2,[3,4],5]
b = list(flatten(a))
print b