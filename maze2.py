import os
import keyboard
import time
import stack as stk
class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", "X", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", " ", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"
    
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
    
    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")
        keyboard.wait("")

    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def checkWay(self):
        posnow = pos(self.ply.y, self.ply.x)
        if self.isInBound(posnow.y-1,posnow.x):
            if self.maze[posnow.y-1][posnow.x] == " " :
                up = 1
            elif self.maze[posnow.y-1][posnow.x] == "E":
                up = 1
            elif self.maze[posnow.y-1][posnow.x] == "X":
                up = 0
            else:
                up = 0
        else:
            up = 0
        if self.isInBound(posnow.y+1,posnow.x):
            if self.maze[posnow.y+1][posnow.x] == " " :
                low = 1
            elif self.maze[posnow.y+1][posnow.x] == "E":
                low = 1
            elif self.maze[posnow.y+1][posnow.x] == "X":
                low = 0
            else:
                low = 0
        else:
            low = 0
        if self.isInBound(posnow.y,posnow.x-1):
            if self.maze[posnow.y][posnow.x-1] == " " :
                lelf = 1
            elif self.maze[posnow.y][posnow.x-1] == "E":
                lelf = 1
            elif self.maze[posnow.y][posnow.x-1] == "X":
                lelf = 0
            else:
                lelf = 0
        else:
            lelf = 0
        if self.isInBound(posnow.y,posnow.x+1):
            if self.maze[posnow.y][posnow.x+1] == " " :
                right = 1
            elif self.maze[posnow.y][posnow.x+1] == "E":
                right = 1
            elif self.maze[posnow.y][posnow.x+1] == "X":
                right = 0
            else:
                right = 0
        else:
            right = 0
        a = waycan(up,low,lelf,right)
        return a



class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

class waycan:

    def __init__(self, u, d, r, l) -> None:
        self.up = u
        self.down = d
        self.right = r
        self.left = l
    
    def sumway(self):
        sumW = self.up+self.down+self.right+self.left
        return sumW



if __name__ == '__main__':

    m = maze()
    m.print()

    posit = pos(m.ply.x,m.ply.y)
    state = False
    
    x = stk.Stack()

    while True:

        if x.peek() == None:
                if m.move_up():
                    m.print()
                    x.push(1)
                    x.push(1)
                else:
                    break
        
        if x.peek() == 1:
                if m.move_up():
                    m.print()
                else:
                    break
        if x.peek() == 2:
                if m.move_left():
                    m.print()
                else:
                    break
        if x.peek() == 3:
                if m.move_down():
                    m.print()
                else:
                    break
        if x.peek() == 4:
                if m.move_right():
                    m.print()
                else:
                    break

        if (posit.x == m.ply.x and posit.y == m.ply.y) :

            if x.peek() == 4:
                x.pop()
                x.push(1)
            elif x.peek() == 3:
                x.pop()
                x.push(4)
            elif x.peek() == 2:
                x.pop()
                if x.peek() != 1:
                    x.push(3)
                else:
                    x.push(4)
            elif x.peek() == 1:
                x.pop()
                x.push(2)
            state = True

        else:
            if state:
                rng = m.checkWay().sumway()
                if rng == 1:
                    m.maze[posit.y][posit.x] = "*"

                second = x._top.item
                first = x._top.next
                x.pop()
                x.pop()
                x.push(first)
                x.push(second)
            
            state = False
            posit.x = m.ply.x
            posit.y = m.ply.y


        print(x.peek())
        time.sleep(0.2)
        # break