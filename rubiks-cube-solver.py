class rubiksCube:
    def __init__(self, size):
        self.size = size

        self.top = []
        for i in range(self.size):
            self.top.append([])
        for j in self.top:
            for k in range(self.size):
                j.append('R')

        self.bottom = []
        for i in range(self.size):
            self.bottom.append([])
        for j in self.bottom:
            for k in range(self.size):
                j.append('O')

        self.front = []
        for i in range(self.size):
            self.front.append([])
        for j in self.front:
            for k in range(self.size):
                j.append('Y')

        self.left = []
        for i in range(self.size):
            self.left.append([])
        for j in self.left:
            for k in range(self.size):
                j.append('G')

        self.back = []
        for i in range(self.size):
            self.back.append([])
        for j in self.back:
            for k in range(self.size):
                j.append('W')

        self.right = []
        for i in range(self.size):
            self.right.append([])
        for j in self.right:
            for k in range(self.size):
                j.append('B')

        self.orientations = {"bottom": self.bottom}

    def __str__(self):
        printStr = ""

        for i in range(self.size):
            printStr += '  ' * self.size * 2
            for j in range(self.size):
                printStr += str(self.bottom[i][j]) + ' '
            printStr += '  ' * self.size * 2
            printStr += '\n'

        for i in range(self.size):
            printStr += '  ' * self.size * 2
            for j in range(self.size):
                printStr += str(self.back[i][j]) + ' '
            printStr += '  ' * self.size * 2
            printStr += '\n'

        for i in range(self.size):
            for j in range(self.size):
                printStr += str(self.bottom[i][j]) + ' ' # need to change order eventually
            for j in range(self.size):
                printStr += str(self.left[i][j]) + ' '
            for j in range(self.size):
                printStr += str(self.top[i][j]) + ' '
            for j in range(self.size):
                printStr += str(self.right[i][j]) + ' '
            for j in range(self.size):
                printStr += str(self.bottom[i][j]) + ' ' # need to change order eventually
            printStr += '\n'

        for i in range(self.size):
            printStr += '  ' * self.size * 2
            for j in range(self.size):
                printStr += str(self.front[i][j]) + ' '
            printStr += '  ' * self.size * 2
            printStr += '\n'

        for i in range(self.size):
            printStr += '  ' * self.size * 2
            for j in range(self.size):
                printStr += str(self.bottom[i][j]) + ' '
            printStr += '  ' * self.size * 2
            printStr += '\n'

        return printStr

xXx = rubiksCube(3)
print(xXx)
