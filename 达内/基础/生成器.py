def fun01():
    for i in range(10):
        value = yield i
        print(value)

generate = fun01()
for item in generate:
    print(item)
    if item%2 ==0:
        generate.send("偶数")