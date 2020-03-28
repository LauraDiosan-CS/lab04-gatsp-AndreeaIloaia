from matplotlib import pyplot as plt

class UI:
    def __init__(self, service):
        self.__service = service

    def main(self):
        self.__service.ga()
        ceva = self.__service.ga()

        plt.plot(ceva)
        plt.show()
