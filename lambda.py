# lambda arguements: expression
byitself = lambda num: num * num

print(byitself(3))

multiply =lambda x, y: x * y
print(multiply(5, 20))

nums = [1,2,3,4,5,6]

squared = map(lambda num: num ** 2, nums)

print(list(squared))