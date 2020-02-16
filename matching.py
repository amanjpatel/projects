# <<Add a small header describing the purpose of the file>>
import numpy.random
import numpy as np

# Describe what the purpose of the variables

array = numpy.random.randint(0,2,(100,10))
test = numpy.random.randint(0,2,(1,10))
match_array = []
print(test)

z = 0
num_matches = 0
allowed_error = int(input("What % allowed error do you want> "))
for y in range(0,100):
    for x in range(0,10):
        num = int(array[y,x])
        num2 = int(test[0,x])
        if num == num2:
            z += 1
        if z >= 10-(allowed_error/10):
            num_matches += 1
            print(array[y])
            match_array.append(array[y])
    z = 0

# Dispaly final calculated result    
print(num_matches)