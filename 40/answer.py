from functools import reduce
import time

start_time = time.time()

tempArray = []
nthArray = [1,10,100,1000,10000,100000,1000000]

concString = ''

for x in range(nthArray[-1]):
    concString += str(x + 1)

counter = 0

for y in concString:
    counter += 1
    if counter in nthArray:
        tempArray.append(int(y))

arrayMultiply = reduce(lambda x, y: x*y, tempArray)

print("Numbers from Nth Position:", tempArray)
print("Multiplied Product:",arrayMultiply)
print("Executed In:",(time.time() - start_time), 'seconds.') #STO 1557571
