class Vertex:
    def __init__(self, city):
        self.city=city
        self.edges = {}
    def add_edge(self, city, weight):
        self.edges[city] = weight
    def get_edges(self):
        return self.edges.keys()
        
class Graph:
    def __init__(self, directed):
        self.vertices = {}
        self.directed = directed
    def add_vertex(self, vertex):
        self.vertices[vertex.city] = vertex

    def add_edge(self, vertex_a, vertex_b, time,price):
        self.vertices[vertex_a.city].add_edge(vertex_b.city, {"time":time,"price":price})
        if not self.directed:
            self.vertices[vertex_b.city].add_edge(vertex_a.city, {"time":time,"price":price})
    def path_exists(self, vertex_a, vertex_b):
        to_visit = [vertex_a]
        visited = []
        while len(to_visit) > 0:
            current = to_visit.pop(0)
            visited.append(current)
            if current == vertex_b:
                return True
            else:
                vertices = self.vertices[current].edges.keys()
                to_visit += [vertex for vertex in vertices if vertex not in visited]
        return False
    def print_graph(self):
        vers=[]
        for i in self.vertices:
            vers.append(i)
        return vers

airline = Graph(directed=True)
kuwait_city = Vertex("Kuwait")
dubai = Vertex("Dubai")
colombo = Vertex("Colombo")
male= Vertex("Male")
doha = Vertex("Doha")
tokyo= Vertex("Tokyo")
oslo = Vertex("Oslo")

airline.add_vertex(kuwait_city)
airline.add_vertex(dubai)
airline.add_vertex(colombo)
airline.add_vertex(male)
airline.add_vertex(doha)
airline.add_vertex(tokyo)
airline.add_vertex(oslo)

airline.add_edge(kuwait_city, dubai,2, 120)
airline.add_edge(kuwait_city, colombo,4, 200)
airline.add_edge(colombo, male,1, 60)
airline.add_edge(dubai, doha,1.5, 100)
airline.add_edge(doha, tokyo,11, 500)
airline.add_edge(dubai, oslo,6, 300)


current_city=input("enter your current city: ")
for cities in airline.vertices[current_city].get_edges():
    print(cities)

to_city=input("choose city you want to travel to: ")
price_time=airline.vertices[current_city].edges[to_city]
print(f"from {current_city} to {to_city} costs: {price_time['price']} and time: {price_time['time']} hours")