import os
import keyboard
import time
class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    [" ", " ", "X", " ", "X", " ", "X"],
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
                self.maze[self.ply.y][self.ply.x] = "1"
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
                self.maze[self.ply.y][self.ply.x] = "1"
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
                self.maze[self.ply.y][self.ply.x] = "1"
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
                self.maze[self.ply.y][self.ply.x] = "1"
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
                up = True
            elif self.maze[posnow.y-1][posnow.x] == "E":
                up = True
            elif self.maze[posnow.y-1][posnow.x] == "X":
                up = False
            else:
                up = False
        else:
            up = False

        if self.isInBound(posnow.y+1,posnow.x):
            if self.maze[posnow.y+1][posnow.x] == " " :
                low = True
            elif self.maze[posnow.y+1][posnow.x] == "E":
                low = True
            elif self.maze[posnow.y+1][posnow.x] == "X":
                low = False
            else:
                low = False
        else:
            low = False

        if self.isInBound(posnow.y,posnow.x-1):
            if self.maze[posnow.y][posnow.x-1] == " " :
                lelf = True
            elif self.maze[posnow.y][posnow.x-1] == "E":
                lelf = True
            elif self.maze[posnow.y][posnow.x-1] == "X":
                lelf = False
            else:
                lelf = False
        else:
            lelf = False

        if self.isInBound(posnow.y,posnow.x+1):
            if self.maze[posnow.y][posnow.x+1] == " " :
                right = True
            elif self.maze[posnow.y][posnow.x+1] == "E":
                right = True
            elif self.maze[posnow.y][posnow.x+1] == "X":
                right = False
            else:
                right = False
        else:
            right = False

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



if __name__ == '__main__':

    m = maze()
    m.print()
    a = m.checkWay()
    print(a.up,a.down,a.left,a.right)

    old_x = m.ply.x 
    old_y = m.ply.y

    # if (old_x == m.ply.x and old_y == m.ply.y) :

    

    while True:
        
        if keyboard.is_pressed("q"):
            print("Quit Program")
            break
        if keyboard.is_pressed("w"):
            if m.move_up():
                m.print()
                a = m.checkWay()
                print(a.up,a.down,a.left,a.right)  
            else:
                break
        if keyboard.is_pressed("s"):
            if m.move_down():
                m.print()
                a = m.checkWay()
                print(a.up,a.down,a.left,a.right)  
            else:
                break
        if keyboard.is_pressed("a"):
            if m.move_left():
                m.print()
                a = m.checkWay()
                print(a.up,a.down,a.left,a.right)  
            else:
                break
        if keyboard.is_pressed("d"):
            if m.move_right():
                m.print()
                a = m.checkWay()
                print(a.up,a.down,a.left,a.right)  
            else:
                break
        # break