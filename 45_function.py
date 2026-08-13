
def sum_all(*args):
    return sum(args)

print(sum_all(1,3,6,2,4,8))

def addi(*args):
    print(*args)
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

print(addi(1,2,3))