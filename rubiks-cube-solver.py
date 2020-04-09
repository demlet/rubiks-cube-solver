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

    def mixUpCube(self):
        print("Currently editing TOP positions. Please input new positions from left to right, top to bottom...")
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 and j == 0:
                    newTopPosition = input("Enter new top left position: ")
                elif i == self.size - 1 and j == self.size - 1:
                    newTopPosition = input("Enter final bottom right position: ")
                else:
                    newTopPosition = input("Enter next position: ")
                self.top[i][j] = newTopPosition
        print("\nCurrently editing BOTTOM positions. Please input new positions from left to right, top to bottom...")
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 and j == 0:
                    newTopPosition = input("Enter new top left position: ")
                elif i == self.size - 1 and j == self.size - 1:
                    newTopPosition = input("Enter final bottom right position: ")
                else:
                    newTopPosition = input("Enter next position: ")
                self.bottom[i][j] = newTopPosition

    def isSolved(self):
        for i in self.top:
            if len(set(i)) > 1:
                return False
        for i in self.bottom:
            if len(set(i)) > 1:
                return False
        for i in self.front:
            if len(set(i)) > 1:
                return False
        for i in self.left:
            if len(set(i)) > 1:
                return False
        for i in self.back:
            if len(set(i)) > 1:
                return False
        for i in self.right:
            if len(set(i)) > 1:
                return False
        return True

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
            for j in range(self.size - 1, -1, -1):
                print(j)
                printStr += str(self.bottom[abs(i - self.size + 1)][j]) + ' ' # need to change order eventually
            for j in range(self.size):
                printStr += str(self.left[i][j]) + ' '
            for j in range(self.size):
                printStr += str(self.top[i][j]) + ' '
            for j in range(self.size):
                printStr += str(self.right[i][j]) + ' '
            for j in range(self.size - 1, -1, -1):
                printStr += str(self.bottom[abs(i - self.size + 1)][j]) + ' ' # need to change order eventually
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

xXx = rubiksCube(2)
print(xXx)
print(xXx.isSolved())
xXx.mixUpCube()
print(xXx)
print(xXx.isSolved())
