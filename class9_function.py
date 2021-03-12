def wash(dry=False, water=8):
    print(f"add water {water} full")
    print("add deterngent")
    print("start wash")
    if dry:
        print("dry cloth")


wash(True)
wash(False, 10)


def add(x=1, y=1):
    return x + y


print(add(3, 2))
print(add(3))
print(add(y=5))


def average(numbers):
    return sum(numbers) / len(numbers)


print(average([1, 2, 3]))
print(average([10, 15, 20]))


def hello(x, y):
    print(x, y)


hello(3, 4)
