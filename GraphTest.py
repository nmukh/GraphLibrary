from Graph import *
from GraphWorld import CircleLayout, GraphWorld



#g = Graph([v,w,v1,v2], [])
#g.add_regular_edges(3)

v = Vertex('v')
w = Vertex('w')
v1= Vertex('v1')
v2 = Vertex('v2')
v3 = Vertex('v3')
v4 = Vertex('v4')
v5 = Vertex('v5')
j = [v,w,v1,v2,v3,v4,v5]  
g = RandomGraph(j)
g.add_random_edges(0)
layout = CircleLayout(g)
# draw the graph
gw = GraphWorld()
gw.show_graph(g, layout)
gw.mainloop()
