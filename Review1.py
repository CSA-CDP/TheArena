#Collin Patterson
#8/25/2016
#Mr. Davis
#Advanced Computer Programming
import random
TimesRun = 10
Numbers = random.randrange(1,50)
RandomNums = []
while TimesRun > 0:
    RandomNums.insert(0,Numbers)
    Numbers = random.randrange(1,50)
    TimesRun = TimesRun - 1
print(RandomNums)
