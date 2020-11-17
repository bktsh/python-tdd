class ProjectEuler:

    def below1000_multiplies_of_3or5(self):
        result = []
        for x in range(1, 1000):
            if x % 3 == 0 or x % 5 == 0:
                result.append(x)
        return result

    def below1000_multiplies_of_3and5(self):
        result = []
        for x in range(1, 1000):
            if x % 3 == 0 and x % 5 == 0:
                result.append(x)
        return result