from functools import reduce
from functools import partial

print(reduce(lambda a,b: a+b, [2,2]))
print(reduce(lambda a,b: a+b, [2,2,2]))
print(reduce(lambda a,b: a+b, range(100)))

power_of_2 = partial(pow, 2)
print(power_of_2(2))
print(power_of_2(5))