# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.x * self.x


# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
#         super().__init__(r, r)

#     def area(self):
#         return 3.14 * super().area()


# A = Shape(4, 4)
# print(A.area())
# c = Circle(5)
# print(c.area())



import heapq

def shortestPath(graph):
    num_nodes = int(graph[0])
    nodes = graph[1:num_nodes+1]
    connections = graph[num_nodes+1:]

    adjacency_list = {}
    for connection in connections:
        start, end, weight = connection.split('|')
        if start not in adjacency_list:
            adjacency_list[start] = []
        adjacency_list[start].append((end, int(weight)))

    heap = [(0, nodes[0], [])]
    visited = set()

    while heap:
        current_weight, current_node, current_path = heapq.heappop(heap)

        if current_node in visited:
            continue

        visited.add(current_node)
        current_path.append(current_node)

        if current_node == nodes[-1]:
            return '-'.join(current_path)

        for neighbor, weight in adjacency_list.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(heap, (current_weight + weight, neighbor, current_path.copy()))

    return -1

# Taking input from the user
user_input = input()
graph = user_input.split(',')

# Calling the function with the provided input
result = shortestPath(graph)
print(result)
