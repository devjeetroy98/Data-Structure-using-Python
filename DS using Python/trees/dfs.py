class Graph:

    visited = set()
    tree={
            # Node and its neighbours
            "A" :["B","C"],
            "B":["D","E"],
            "C":[],
            "D":["F"],
            "E":[],
            "F":[]
    }

    def dfs(self,node):
            self.visited.add(node)
            print(node, end=" ")
            for i in self.tree[node]:
                self.dfs(i)


if __name__ =="__main__":
    g = Graph()
    g.dfs("A")
    print()