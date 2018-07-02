import random
import math
import time

count = 0
start = time.clock()

# change num candidate to test
numcandidate = 1000

for j in range(10000):
    candidate = list()
    for i in range(numcandidate):
        candidate.append(i)
    random.shuffle(candidate)
    samplesize = round(len(candidate) * math.exp(-1))
    sample = candidate[ : samplesize]
    benchmark = min(sample)
    best = 0
    index = samplesize
    while index <= len(candidate) - 1:
        if candidate[index] <= benchmark:
            best = index
            if candidate[best] == min(candidate):
                count += 1
            break
        index += 1

end = time.clock()
print("probability is ", count / numcandidate)
print("running time is ", end - start)
