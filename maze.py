from PIL import Image
import numpy as np

class point:
    def __init__(self, is_border, is_door):
        self.taken = False
        self.is_border = is_border
        self.is_door = is_door

    def take(self, depth):
        self.taken = True
        self.depth = depth
    
class wave:
    def __init__(self):
        self.fronts = []

    def add_front(self,x,y):
        self.fronts.append([x,y])

    
    def next_step(self, arr):
        for i in range(0, len(self.fronts)):
            arr[self.fronts[i][0],self.fronts[i][1]].take(1)
        
        t = self.fronts
        self.fronts = [[]]
        for i in range(0,len(t)):
            x = t[i][0]
            y = t[i][1]

            if arr[x+1][y+1].is_border == False and arr[x+1][y+1].taken == False:
                self.fronts.


            
            



class maze:
    def __init__(self,file):
        self.w = wave()
        self.arr = self.open_file(file)


    def open_file(self, file):
        self.img = Image.open(file).convert('L')
        a = np.array(self.img)
        arr = [[]]
        t = []
        for i in range(0,len(a)):
            for j in range(0,len(a[0])):
                if a[i][j] == 0:
                    arr[i].append(point(True,False))
                else:
                    if i == 0 or j == 0 or i == len(a)-1 or j == len(a[0])-1:
                        arr[i].append(point(False, True))
                        t.append(i)
                        t.append(j)
                    else:
                        arr[i].append(point(False, False))
            arr.append([])
        arr[t[0]][t[1]].take(1)
        if t[0] == 0:
            self.w.add_front(t[0]+1, t[1])
        elif t[0] == len(arr):
            self.w.add_front(t[0]-1, t[1])
        elif t[1] == 0:
            self.w.add_front(t[0], t[1]+1)
        elif t[1] == len(arr[0]):
            self.w.add_front(t[0], t[1]-1)

        
        return arr

a = maze('maze.png')