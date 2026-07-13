# import random
# import statistics

# #population : marks of all 10 students in the class

# population = [50,60,65,70,72,75,80,85,90,95]

# print("population:", population)
# print("population size:", len(population))
# print("population mean:", statistics.mean(population))


# # sample: randomly pick 4 students out of the population

# random.seed(1)                               
# # yeh same sample generate karne ke liye hai agr yeh na hua to har bar alag sample generate hoga

# sample= random.sample(population, 4)
# print("Random sample:", sample)



#how production code looks like (debugging)

import random
import statistics

population = [50,60,65,70,72,75,80,85,90,95]
random.seed(1)                               
sample= random.sample(population, 4)


# print("population:", population)
# print("population size:", len(population))
# print("population mean:", statistics.mean(population))
# print("Random sample:", sample)