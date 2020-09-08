import random
# import time
from timeit import default_timer as timer

start = timer()
# ...
# print(end - start)

# print("hello")
arr = ['Danny', 'Scott', 'Yannick', 'Toph', 'Pat', 'Labau', 'Reese', 'Teddy']

# print(random.shuffle(arr))

# start = time.time()
# random.shuffle(x := list(arr))
# x = "".join(x)
# print(x)
i = 0
while i < 240000:
   random.shuffle(x := list(arr))
   i += 1

end = timer()
# end = time.time()
print(end - start)
print(x)
