from chromosome import Chromosome
from ga import GA


class Service:
    def __init__(self, repo):
        self.__repo = repo
        self.__probParam = {'function': self.__fitness_distance, 'noNodes': 0, 'mat': [], 'pool': []}
        self.__param = {'popSize': 80}

    def ga(self):
        network = self.__repo.read_file()
        self.__probParam['noNodes'] = network['noNodes']
        self.__probParam['mat'] = network['mat']
        ga = GA(self.__param, self.__probParam)
        ga.initialisation()
        ga.evaluation()
        g = 0
        fitnessuri = []
        while g < 500:
            # ga.oneGenerationElitism()
            ga.oneGenerationElitism2()
            g += 1
            best_chromo = ga.bestChromosome()
            print('Best solution in generation ' + str(g) + ' is: x = ' + str(best_chromo.repres) + '\nhas fit: ' + str(
                best_chromo.fitness) + '\n')
            fitnessuri.append(best_chromo.fitness)

        return fitnessuri

    @staticmethod
    def __fitness_distance(path, mat):
        fit = 0
        copy = path
        for i in range(len(copy) - 1):
            fit += mat[copy[i]][copy[i + 1]]
        fit += mat[copy[-1]][copy[0]]
        return fit
