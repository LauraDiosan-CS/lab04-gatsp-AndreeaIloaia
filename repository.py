from math import sqrt


class Repository:
    def __init__(self, file_path):
        self.__file_path = file_path

    def read_file(self):
        if "berlin" in self.__file_path:
            return self.__read_b()
        else:
            return self.__read()

    def __read(self):
        network = {}
        file = open(self.__file_path, "r")
        text = file.read()
        linii = text.split("\n")
        lungime = int(linii[0])
        network['noNodes'] = lungime
        matrice = []
        for i in range(1, lungime + 1):
            linie = linii[i].split(",")
            mat = []
            for j in linie:
                mat.append(int(j))
            matrice.append(mat)
        network['mat'] = matrice
        return network

    @staticmethod
    def __euclid(x, y):
        return sqrt((y[0] - x[0]) * (y[0] - x[0]) + (y[1] - x[1]) * (y[1] - x[1]))

    def __read_b(self):
        network = {}
        f = open(self.__file_path, "r")
        text = f.read().split("\n")

        lungime = int(text[3].split(':')[1])
        network['noNodes'] = lungime
        f.readline()
        f.readline()
        lines = []
        for i in range(6, lungime + 6):
            linie = text[i].split(" ")
            lines.append((float(linie[1]), float(linie[2])))

        mat = [[0.0 for i in range(lungime)] for i in range(lungime)]

        for i in range(0, lungime - 1):
            for j in range(i + 1, lungime):
                mat[j][i] = mat[i][j] = self.__euclid(lines[i], lines[j])
        network['mat'] = mat
        return network
