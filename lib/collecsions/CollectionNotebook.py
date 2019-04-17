class CollectionNotebook(object):

    def fibSeriesUptoN(self, maxNum):
        a, b = 1, 1
        result = [a, b]
        while b < maxNum:
            a = b
            b = a + b
            result.append(b)
        return result

    def pow4OfList(self, list):
        return [ i ** 4 for i in list]