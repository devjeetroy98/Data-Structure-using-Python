class Graph:

    visited = list()
    queue = list()
    tree={
            # Node and its neighbours
            "A" :["B","C"],
            "B":["D","E"],
            "C":[],
            "D":["F"],
            "E":[],
            "F":[]
    }

    def bfs(self,node):
            self.visited.append(node)
            self.queue.append(node)

            while self.queue:
                now = self.queue.pop(0)
                print(now, end=" ")
            
                for i in self.tree[now]:
                    if i not in self.visited:
                        self.queue.append(i)
                        self.visited.append(i)


if __name__ =="__main__":
    g = Graph()
    g.bfs("A")
    print()