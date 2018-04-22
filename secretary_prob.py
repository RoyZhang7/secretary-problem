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
    # the value of the list is the rank of the candidates

    # print ("rank ")
    # print (candidate)

    samplesize = round(len(candidate) * math.exp(-1))
    # another method is selecting sqrt(n) sample
    # print ("sample size is " + str(samplesize))

    sample = candidate[ : samplesize]

    benchmark = min(sample)
    # print ("best of the sample is " + str(benchmark))
    best = 0
    index = samplesize
    while index <= len(candidate) - 1:
        if candidate[index] <= benchmark:
            best = index
            if candidate[best] == min(candidate):
                count += 1
            break
        index += 1
    # if candidate[best] <= benchmark:
        # count += 1
        # print ("Best candidate found is " + str(index+1) + " with talent " + str(candidate[index]))
    # else:
        # print ("Could not find a best candidate")
    # except:
        # print("Could not find a best candidate")
end = time.clock()
print("probability is ", count / numcandidate)
print("running time is ", end - start)
