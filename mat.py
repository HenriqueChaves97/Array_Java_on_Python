class Array():
    def __init__(self, c,l):
        self.linha = c[0]
        self.coluna = l[0]
        self.lista = list()

    def int(self):
        self.generate_line = [0]*self.linha
        for i in range(0, self.coluna):
            self.lista.append(self.generate_line)
        return self.lista

    def str(self):
        self.generate_line = ['']*self.linha
        for i in range(0, self.coluna):
            self.lista.append(self.generate_line)
        return self.lista

print(Array([2],[3]).str())
print(Array([4],[2]).int())

        
        
