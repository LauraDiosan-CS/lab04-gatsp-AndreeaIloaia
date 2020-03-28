from random import randint, random, shuffle
from chromosome import Chromosome

class GA:
    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            path = c.repres
            shuffle(path)
            c.repres = path
            self.__population.append(c)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres, self.__problParam['mat'])

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness < best.fitness:
                best = c
        return best

    def bestChromosome2(self, list):
        best = list[0]
        for c in list:
            if c.fitness < best.fitness:
                best = c
        list.remove(best)
        return best, list

    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness > best.fitness:
                best = c
        return best

    def selection(self):
        pos1 = randint(0, self.__param['popSize'] - 1)
        pos2 = randint(0, self.__param['popSize'] - 1)
        if self.__population[pos1].fitness < self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def selection2(self):
        self.__problParam['pool'].clear()
        sum = 0
        sums = []
        prob = []
        for i in range(len(self.__population)):
            sum += self.__population[i].fitness
            sums.append(sum)
        for i in sums:
            prob.append((i / sum))

        for i in range(self.__param['popSize'] // 2):
            roulette = random()

            for j, p in enumerate(prob):
                if roulette < p:
                    self.__problParam['pool'].append(self.__population[i])
                    return i


    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['popSize'] - 1):
            p1 = self.__population[self.selection2()]
            p2 = self.__population[self.selection2()]
            off = p1.crossover(p2)
            off.mutation2()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism2(self):
        newPop = []
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection2()]
            p2 = self.__population[self.selection2()]
            off = p1.crossover_nwox(p2)
            off.mutation2()
            newPop.append(off)
        newGen = []
        copy = self.__population
        for i in range(self.__param['popSize'] // 2):
            best, copy = self.bestChromosome2(copy)
            newGen.append(best)
        copy = newPop
        for j in range(self.__param['popSize'] // 2, self.__param['popSize']):
            best, copy = self.bestChromosome2(copy)
            newGen.append(best)
        self.__population = newGen
        self.evaluation()
