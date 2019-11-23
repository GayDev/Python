class movie:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def overlaps(self,movie):
        if (self.end >= movie.end and self.start <= movie.end) or (self.start <= movie.start and self.end >= movie.start):
            return True
        else:
            return False
    
n = int(input())
a = []
b = []
path = []

for i in range(0,n):
    inp = input()
    start = int(inp.split(' ')[0])
    end = int(inp.split(' ')[1])
    a.append(movie(start,end))

for i in range(0,len(a)):
    if len(a) == 0:
        break
    min_endpoint = a[0].end
    index = 0

    for i in range(0,len(a)):
        if a[i].end < min_endpoint:
            min_endpoint=a[i].end
            index = i

    path.append(a[index])
    for i in range(0,len(a)):
        if (a[index].overlaps(a[i]) == False):
            b.append(a[i])

    a = b
    b = []

print()

for i in range(0,len(path)):
    print(path[i].start, end = '\t')
    print(path[i].end)
