# Anonymous Functions or Lambda

# Example 1
f = lambda a, b : a + b
print(f(2, 5))


# Example 2
nums = [3,4,5,7,1,8,0,12,22]

# use of filter:: filter(function, list)
evens =  list(filter(lambda n: n%2==0, nums))
print('Evens:: ', evens)

# use of map:: map(function, list)
doubles =  list(map(lambda n : n*2, evens))
print('Doubles:: ', doubles)

# use of reduce:: reduce(function, list)
reduce =  reduce(lambda a,b : a + b, doubles)
print('Reduce:: ', reduce)




