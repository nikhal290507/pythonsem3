import random
import statistics

#population : marks of all 10 students in the class

population = [50,60,65,70,72,75,80,85,90,95]

print("population:", population)
print("population size:", len(population))
print("population mean:", statistics.mean(population))


# sample: randomly pick 4 students out of the population

random.seed(1)
sample= random.sample(population, 4)
print("Random sample:", sample)