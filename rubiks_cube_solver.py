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

    def rotateAdjacentSidePos(self, side):
        currentRing = 0
        while currentRing < self.size // 2:
            topRowCopy = []
            for i in range(currentRing, self.size - currentRing): #temporary storing of top row
                topRowCopy.append(side[currentRing][i])
            for i in range(currentRing, self.size - currentRing): #move right column to top row
                side[currentRing][i] = side[i][self.size - currentRing - 1]
            for i in range(currentRing, self.size - currentRing): #move bottom row to right column
                side[i][self.size - currentRing - 1] = side[self.size - currentRing - 1][abs(i - (self.size - 1))]
            for i in range(currentRing, self.size - currentRing): #move left column to bottom row
                side[self.size - currentRing - 1][abs(i - (self.size - 1))] = side[abs(i - (self.size - 1))][currentRing]
            j = 0 #move copy of top row to left column
            for i in range(currentRing, self.size - currentRing):
                side[abs(i - (self.size - 1))][currentRing] = topRowCopy[j]
                j += 1
            currentRing += 1

    def rotateAdjacentSideNeg(self, side):
        currentRing = 0
        while currentRing < self.size // 2:
            topRowCopy = []
            for i in range(currentRing, self.size - currentRing): #temporary storing of top row
                topRowCopy.append(side[currentRing][i])
            for i in range(currentRing, self.size - currentRing): #move left column to top row
                side[currentRing][i] = side[abs(i - (self.size - 1))][currentRing]
            for i in range(currentRing, self.size - currentRing): #move bottom row to left column
                side[i][currentRing] = side[self.size - currentRing - 1][i]
            for i in range(currentRing, self.size - currentRing): #move right column to bottom row
                side[self.size - currentRing - 1][i] = side[abs(i - (self.size - 1))][self.size - currentRing - 1]
            j = 0 #move copy of top row to right column...
            for i in range(currentRing, self.size - currentRing):
                side[i][self.size - currentRing - 1] = topRowCopy[j]
                j += 1
            currentRing += 1

    def rotateXLeft(self, row):
        bottomReversed = self.bottom[abs(self.size - 1 - row)].copy()
        bottomReversed.reverse()
        self.bottom[abs(self.size - 1 - row)] = self.left[row].copy()
        self.bottom[abs(self.size - 1 - row)].reverse()
        self.left[row] = self.top[row].copy()
        self.top[row] = self.right[row].copy()
        self.right[row] = bottomReversed
        if row == 0:
            self.rotateAdjacentSideNeg(self.back)
        if row == self.size - 1:
            self.rotateAdjacentSidePos(self.front)

    def rotateXRight(self, row):
        bottomReversed = self.bottom[abs(self.size - 1 - row)].copy()
        bottomReversed.reverse()
        self.bottom[abs(self.size - 1 - row)] = self.right[row].copy()
        self.bottom[abs(self.size - 1 - row)].reverse()
        self.right[row] = self.top[row].copy()
        self.top[row] = self.left[row].copy()
        self.left[row] = bottomReversed
        if row == 0:
            self.rotateAdjacentSidePos(self.back)
        if row == self.size - 1:
            self.rotateAdjacentSideNeg(self.front)

    def rotateYUp(self, column):
        bottomColumnCopy = []
        for i in range(self.size):
            bottomColumnCopy.append(self.bottom[i][column])
        for i in range(self.size):
            self.bottom[i][column] = self.back[i][column]
            self.back[i][column] = self.top[i][column]
            self.top[i][column] = self.front[i][column]
            self.front[i][column] = bottomColumnCopy[i]
        if column == 0:
            self.rotateAdjacentSidePos(self.left)
        if column == self.size - 1:
            self.rotateAdjacentSideNeg(self.right)

    def rotateYDown(self, column):
        bottomColumnCopy = []
        for i in range(self.size):
            bottomColumnCopy.append(self.bottom[i][column])
        for i in range(self.size):
            self.bottom[i][column] = self.front[i][column]
            self.front[i][column] = self.top[i][column]
            self.top[i][column] = self.back[i][column]
            self.back[i][column] = bottomColumnCopy[i]
        if column == 0:
            self.rotateAdjacentSideNeg(self.left)
        if column == self.size - 1:
            self.rotateAdjacentSidePos(self.right)

    def rotateZPos(self, row):
        frontRowCopy = []
        for i in range(self.size):
            frontRowCopy.append(self.front[row][i])
        for i in range(self.size):
            self.front[row][i] = self.left[i][abs(row - (self.size - 1))]
            self.left[i][abs(row - (self.size - 1))] = self.back[abs(row - (self.size - 1))][abs(i - (self.size - 1))]
            self.back[abs(row - (self.size - 1))][abs(i - (self.size - 1))] = self.right[abs(i - (self.size - 1))][row]
            self.right[abs(i - (self.size - 1))][row] = frontRowCopy[i]
        if row == 0:
            self.rotateAdjacentSidePos(self.top)
        if row == self.size - 1:
            self.rotateAdjacentSideNeg(self.bottom)

    def rotateZNeg(self, row):
        frontRowCopy = []
        for i in range(self.size):
            frontRowCopy.append(self.front[row][i])
        for i in range(self.size):
            self.front[row][i] = self.right[abs(i - (self.size - 1))][row]
            self.right[abs(i - (self.size - 1))][row] = self.back[abs(row - (self.size - 1))][abs(i - (self.size - 1))]
            self.back[abs(row - (self.size - 1))][abs(i - (self.size - 1))] = self.left[i][abs(row - (self.size - 1))]
            self.left[i][abs(row - (self.size - 1))] = frontRowCopy[i]
        if row == 0:
            self.rotateAdjacentSideNeg(self.top)
        if row == self.size - 1:
            self.rotateAdjacentSidePos(self.bottom)

    def mixUpCube(self):
        positCount = 0
        print("Currently editing TOP positions.\nPlease input new positions as a single character from left to right, top to bottom (enter \"\\s\" to skip this position, enter \"\\n\" to skip to next side, enter \"\\q\" to stop editing completely)...\n")
        for i in range(self.size):
            for j in range(self.size):
                newPosition = ""
                while newPosition == "":
                    if i == 0 and j == 0:
                        newPosition = input("Enter new top left position (%d): " % positCount)
                    elif i == self.size - 1 and j == self.size - 1:
                        newPosition = input("Enter final bottom right position (%d): " % positCount)
                    else:
                        newPosition = input("Enter next position (%d): " % positCount)
                    if len(newPosition) > 1 and (newPosition != '\\s' and newPosition != '\\n' and newPosition != '\\q'):
                        print("\nTHAT WAS NOT A VALID INPUT...\n\nCurrently editing TOP positions.\nPlease input new positions as a single character from left to right, top to bottom (enter \"\\s\" to skip this position, enter \"\\n\" to skip to next side, enter \"\\q\" to stop editing completely)...\n")
                        newPosition = ""
                    elif newPosition == "\\n":
                        break
                    elif newPosition == "\\q":
                        return "\nEditing Completed!"
                    elif newPosition == "\s":
                        positCount += 1
                    else:
                        self.top[i][j] = newPosition
                        positCount += 1
                if newPosition == "\\n":
                    break
            if newPosition == "\\n":
                break
        print("\nCurrently editing BOTTOM positions.\nPlease input new positions as a single character from left to right, top to bottom (enter \"\\s\" to skip this position, enter \"\\n\" to skip to next side, enter \"\\q\" to stop editing completely)...\n")
        positCount = 0
        for i in range(self.size):
            for j in range(self.size):
                newPosition = ""
                while newPosition == "":
                    if i == 0 and j == 0:
                        newPosition = input("Enter new top left position (%d): " % positCount)
                    elif i == self.size - 1 and j == self.size - 1:
                        newPosition = input("Enter final bottom right position (%d): " % positCount)
                    else:
                        newPosition = input("Enter next position (%d): " % positCount)
                    if len(newPosition) > 1 and (newPosition != '\\s' and newPosition != '\\n' and newPosition != '\\q'):
                        print("\nTHAT WAS NOT A VALID INPUT...\n\nCurrently editing BOTTOM positions.\nPlease input new positions as a single character from left to right, top to bottom (enter \"\\s\" to skip this position, enter \"\\n\" to skip to next side, enter \"\\q\" to stop editing completely)...\n")
                        newPosition = ""
                    elif newPosition == "\\n":
                        break
                    elif newPosition == "\\q":
                        return "\nEditing Completed!"
                    elif newPosition == "\s":
                        positCount += 1
                    else:
                        self.bottom[i][j] = newPosition
                        positCount += 1
                if newPosition == "\\n":
                    break
            if newPosition == "\\n":
                break
        print("\nCurrently editing FRONT positions.\nPlease input new positions as a single character from left to right, top to bottom (enter \"\\s\" to skip this position, enter \"\\n\" to skip to next side, enter \"\\q\" to stop editing completely)...\n")
        positCount = 0
        for i in range(self.size):
            for j in range(self.size):
                newPosition = ""
                while newPosition == "":
                    if i == 0 and j == 0:
                        newPosition = input("Enter new top left position (%d): " % positCount)
                    elif i == self.size - 1 and j == self.size - 1:
                        newPosition = input("Enter final bottom right position (%d): " % positCount)
                    else:
                        newPosition = input("Enter next position (%d): " % positCount)
                    if len(newPosition) > 1 and (newPosition != '\\s' and newPosition != '\\n' and newPosition != '\\q'):
                        print("\nTHAT WAS NOT A VALID INPUT...\n\nCurrently editing FRONT positions.\nPlease input new positions as a single character from left to right, top to bottom (enter \"\\s\" to skip this position, enter \"\\n\" to skip to next side, enter \"\\q\" to stop editing completely)...\n")
                        newPosition = ""
                    elif newPosition == "\\n":
                        break
                    elif newPosition == "\\q":
                        return "\nEditing Completed!"
                    elif newPosition == "\s":
                        positCount += 1
                    else:
                        self.front[i][j] = newPosition
                        positCount += 1
                if newPosition == "\\n":
                    break
            if newPosition == "\\n":
                break
        print("\nCurrently editing LEFT positions.\nPlease input new positions as a single character from left to right, top to bottom (enter \"\\s\" to skip this position, enter \"\\n\" to skip to next side, enter \"\\q\" to stop editing completely)...\n")
        positCount = 0
        for i in range(self.size):
            for j in range(self.size):
                newPosition = ""
                while newPosition == "":
                    if i == 0 and j == 0:
                        newPosition = input("Enter new top left position (%d): " % positCount)
                    elif i == self.size - 1 and j == self.size - 1:
                        newPosition = input("Enter final bottom right position (%d): " % positCount)
                    else:
                        newPosition = input("Enter next position (%d): " % positCount)
                    if len(newPosition) > 1 and (newPosition != '\\s' and newPosition != '\\n' and newPosition != '\\q'):
                        print("\nTHAT WAS NOT A VALID INPUT...\nCurrently editing LEFT positions.\nPlease input new positions as a single character from left to right, top to bottom (enter \"\\s\" to skip this position, enter \"\\n\" to skip to next side, enter \"\\q\" to stop editing completely)...\n")
                        newPosition = ""
                    elif newPosition == "\\n":
                        break
                    elif newPosition == "\\q":
                        return "\nEditing Completed!"
                    elif newPosition == "\s":
                        positCount += 1
                    else:
                        self.left[i][j] = newPosition
                        positCount += 1
                if newPosition == "\\n":
                    break
            if newPosition == "\\n":
                break
        print("\nCurrently editing BACK positions.\nPlease input new positions as a single character from left to right, top to bottom (enter \"\\s\" to skip this position, enter \"\\n\" to skip to next side, enter \"\\q\" to stop editing completely)...\n")
        positCount = 0
        for i in range(self.size):
            for j in range(self.size):
                newPosition = ""
                while newPosition == "":
                    if i == 0 and j == 0:
                        newPosition = input("Enter new top left position (%d): " % positCount)
                    elif i == self.size - 1 and j == self.size - 1:
                        newPosition = input("Enter final bottom right position (%d): " % positCount)
                    else:
                        newPosition = input("Enter next position (%d): " % positCount)
                    if len(newPosition) > 1 and (newPosition != '\\s' and newPosition != '\\n' and newPosition != '\\q'):
                        print("\nTHAT WAS NOT A VALID INPUT...\nCurrently editing BACK positions.\nPlease input new positions as a single character from left to right, top to bottom (enter \"\\s\" to skip this position, enter \"\\n\" to skip to next side, enter \"\\q\" to stop editing completely)...\n")
                        newPosition = ""
                    elif newPosition == "\\n":
                        break
                    elif newPosition == "\\q":
                        return "\nEditing Completed!"
                    elif newPosition == "\s":
                        positCount += 1
                    else:
                        self.back[i][j] = newPosition
                        positCount += 1
                if newPosition == "\\n":
                    break
            if newPosition == "\\n":
                break
        print("\nCurrently editing RIGHT positions.\nPlease input new positions as a single character from left to right, top to bottom (enter \"\\s\" to skip this position, enter \"\\n\" to skip to next side, enter \"\\q\" to stop editing completely)...\n")
        positCount = 0
        for i in range(self.size):
            for j in range(self.size):
                newPosition = ""
                while newPosition == "":
                    if i == 0 and j == 0:
                        newPosition = input("Enter new top left position (%d): " % positCount)
                    elif i == self.size - 1 and j == self.size - 1:
                        newPosition = input("Enter final bottom right position (%d): " % positCount)
                    else:
                        newPosition = input("Enter next position (%d): " % positCount)
                    if len(newPosition) > 1 and (newPosition != '\\s' and newPosition != '\\n' and newPosition != '\\q'):
                        print("\nTHAT WAS NOT A VALID INPUT...\nCurrently editing RIGHT positions.\nPlease input new positions as a single character from left to right, top to bottom (enter \"\\s\" to skip this position, enter \"\\n\" to skip to next side, enter \"\\q\" to stop editing completely)...\n")
                        newPosition = ""
                    elif newPosition == "\\n":
                        break
                    elif newPosition == "\\q":
                        return "\nEditing Completed!"
                    elif newPosition == "\s":
                        positCount += 1
                    else:
                        self.right[i][j] = newPosition
                        positCount += 1
                if newPosition == "\\n":
                    break
            if newPosition == "\\n":
                break

        return "\nEditing Completed!"

    def isSolved(self):
        check = self.top[0][0]
        for i in self.top:
            if set(check) != set(i):
                return False
        check = self.bottom[0][0]
        for i in self.bottom:
            if set(check) != set(i):
                return False
        check = self.front[0][0]
        for i in self.front:
            if set(check) != set(i):
                return False
        check = self.left[0][0]
        for i in self.left:
            if set(check) != set(i):
                return False
        check = self.back[0][0]
        for i in self.back:
            if set(check) != set(i):
                return False
        check = self.right[0][0]
        for i in self.right:
            if set(check) != set(i):
                return False
        return True

    def isSameAs(self, other):
        if self.top == other.top and self.bottom == other.bottom and self.front == other.front \
        and self.left == other.left and self.back == other.back and self.right == other.right:
            return True
        return False

    def copyCube(self, other):
        for i in range(self.size):
            other.top[i] = self.top[i].copy()
            other.bottom[i] = self.bottom[i].copy()
            other.front[i] = self.front[i].copy()
            other.left[i] = self.left[i].copy()
            other.back[i] = self.back[i].copy()
            other.right[i] = self.right[i].copy()

    def exportCube(self, filepath):
        with open(filepath, 'w') as f:
            for i in range(self.size):
                for j in range(self.size):
                    f.writelines(self.top[i][j] + '\n')
            for i in range(self.size):
                for j in range(self.size):
                    f.writelines(self.bottom[i][j] + '\n')
            for i in range(self.size):
                for j in range(self.size):
                    f.writelines(self.front[i][j] + '\n')
            for i in range(self.size):
                for j in range(self.size):
                    f.writelines(self.left[i][j] + '\n')
            for i in range(self.size):
                for j in range(self.size):
                    f.writelines(self.back[i][j] + '\n')
            for i in range(self.size):
                for j in range(self.size):
                    f.writelines(self.right[i][j] + '\n')
            f.close

    def importCube(self, filepath):
        with open(filepath, 'r') as f:
            for i in range(self.size):
                for j in range(self.size):
                    self.top[i][j] = str(f.readline())[:-1]
            for i in range(self.size):
                for j in range(self.size):
                    self.bottom[i][j] = str(f.readline())[:-1]
            for i in range(self.size):
                for j in range(self.size):
                    self.front[i][j] = str(f.readline())[:-1]
            for i in range(self.size):
                for j in range(self.size):
                    self.left[i][j] = str(f.readline())[:-1]
            for i in range(self.size):
                for j in range(self.size):
                    self.back[i][j] = str(f.readline())[:-1]
            for i in range(self.size):
                for j in range(self.size):
                    self.right[i][j] = str(f.readline())[:-1]
            f.close

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
                printStr += str(self.bottom[abs(i - self.size + 1)][j]) + ' '
            for j in range(self.size):
                printStr += str(self.left[i][j]) + ' '
            for j in range(self.size):
                printStr += str(self.top[i][j]) + ' '
            for j in range(self.size):
                printStr += str(self.right[i][j]) + ' '
            for j in range(self.size - 1, -1, -1):
                printStr += str(self.bottom[abs(i - self.size + 1)][j]) + ' '
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
xXx.importCube("myCube3x3.cub")
print(xXx)
xXx.mixUpCube()
print(xXx)
# xXx.save("myCube6x6.cub")
# xXx.rotateYDown(0)
# xXx.rotateYDown(1)
# xXx.rotateZNeg(2)
# print(xXx)
