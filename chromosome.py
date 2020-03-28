from random import randint


def generateARandomPermutation(n):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm


# permutation-based representation
class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam  # problParam has to store the number of nodes/cities
        self.__repres = generateARandomPermutation(self.__problParam['noNodes'])
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0):
        self.__fitness = fit

    def renumber(self):
        for i in range(self.__problParam['noNodes']):
            self.__repres[i] += 1

    def crossover(self, c):
        # order XO
        pos1 = randint(-1, self.__problParam['noNodes'] - 1)
        pos2 = randint(-1, self.__problParam['noNodes'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2]
        for el in c.__repres[pos2:] + c.__repres[:pos2]:
            if el not in newrepres:
                if len(newrepres) < self.__problParam['noNodes'] - pos1:
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1
        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        return offspring

    def crossover_nwox(self, p2):
        # Non wrapping order XO
        p1 = self.__repres
        offspring = Chromosome(self.__problParam)
        pos1 = randint(0, self.__problParam['noNodes'] - 1)
        pos2 = randint(0, self.__problParam['noNodes'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        child = [-1 for i in range(self.__problParam['noNodes'])]
        child[pos1: pos2 + 1] = p1[pos1: pos2 + 1]

        p = c = 0
        while p < self.__problParam['noNodes']:
            if pos1 <= c <= pos2:
                c = pos2 + 1
                continue

            gene = p2.repres[p]

            if gene in child:
                p += 1
                continue
            else:
                child[c] = gene
                c += 1
                p += 1

        offspring.repres = child
        return offspring

    def mutation(self):
        # insert mutation
        pos1 = randint(0, self.__problParam['noNodes'] - 1)
        pos2 = randint(0, self.__problParam['noNodes'] - 1)
        while pos1 == pos2:
            pos2 = randint(0, self.__problParam['noNodes'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)

    def mutation2(self):
        # invert mutation
        pos1 = randint(0, self.__problParam['noNodes'] - 1)
        pos2 = randint(0, self.__problParam['noNodes'] - 1)
        while pos1 == pos2:
            pos2 = randint(0, self.__problParam['noNodes'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        while pos1 < pos2:
            el = self.__repres[pos2]
            del self.__repres[pos2]
            self.__repres.insert(pos1 + 1, el)
            el = self.__repres[pos1]
            del self.__repres[pos1]
            self.__repres.insert(pos2, el)
            pos1 += 1
            pos2 -= 1

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness

    def __lt__(self, other):
        return self.__fitness < other.fitness
