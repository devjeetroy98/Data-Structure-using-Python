class Graph:

    visited = list()
    queue = list()
    sumx=0
    tree={
            # Node and its neighbours
            "1" :["2","3"],
            "2":["4","5"],
            "3":[],
            "4":["6"],
            "5":[],
            "6":[]
    }

    def findSome(self, start):

        self.visited.append(start)
        self.queue.append(start)
        self.sumx = int(start)
        
        while self.queue:
            s = self.queue.pop(0)
            for i in self.tree[s]:
                if i not in self.visited:
                    self.visited.append(i)
                    self.queue.append(i)
                    self.sumx += int(i)

if __name__ =="__main__":
    g = Graph()
    g.findSome("1")
    print(g.sumx)