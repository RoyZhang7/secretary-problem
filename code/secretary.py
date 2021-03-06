#TODO:
# 1)Testing
# 2)Implementation of other strategies. Analysis and comperation.
# 3)Provide math induction of optimal solution.
#FIXME:
# None

import random
import math

candidate = list()
for i in range(1000):
    candidate.append(random.randint(1,100))

print ("talent ")
print (candidate)

samplesize = round(len(candidate) * math.exp(-1))
# another method is selecting sqrt(n) sample
print ("sample size is " + str(samplesize))

sample = candidate[ : samplesize]

benchmark = max(sample)
print ("maximum of the sample is " + str(benchmark))
best = 0
index = samplesize
while index <= len(candidate)-1:
    if candidate[index] >= benchmark:
        best = index
        break
    index += 1
if candidate[best] >= benchmark:
    print ("Best candidate found is " + str(index+1) + " with talent " + str(candidate[index]))
else:
    print ("Could not find a best candidate")
