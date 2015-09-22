class EfficientFib(object):
    cache = {}

    def calc(self, n):
        if n < 2:
            return n

        if n in self.cache:
            return self.cache[n]
        else:
            fibn = self.calc(n-1) + self.calc(n-2)
            self.cache[n] = fibn
            return fibn

efib = EfficientFib()
print(efib.calc(40))
