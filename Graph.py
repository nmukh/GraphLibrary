# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """create a new graph.  (vs) is a list of vertices;
        (es) is a list of edges."""
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """add (v) to the graph"""
        self[v] = {}

    def add_edge(self, e):
        """add (e) to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e
        
    def get_edge(self, v1, v2):
        try:
            if self[v1][v2] == self[v2][v1]:
                return self[v1][v2]
        except:
            return None
    
    def remove_edge(self, e):
        try:
            del self[e[0]][e[1]]
            del self[e[1]][e[0]]
        except:
            print("Edge does not exist")
        
    def vertices(self):
        return self.keys()
    
    def edges(self):
        edges = []
        try:
            for item in self.values():
                edges.append(item.values()[0])
            return list(set(edges))
        except:
            return None
    
    def out_vertices(self, vertex):
        return self[vertex].keys()
        
    def out_edges(self, vertex):
        return self[vertex].values()
    
    def add_all_edges(self):
        for v1 in self.vertices():
            for v2 in self.vertices():
                if v1 != v2:
                    self.add_edge(Edge(v1, v2))
        return self

    #Handshaking Lemma Sum(Deg(v_k))= 2*|e|
    def add_regular_edges(self, degree):
        #import pdb; pdb.set_trace()
        if degree * len(self.vertices()) % 2 == 0:
            for vertex_from in self.vertices():
                if len(self.out_vertices(vertex_from))< degree:
                    for vertex_to in self.vertices():
                        if (vertex_to != vertex_from) and (len(self.out_vertices(vertex_to)) < degree) and not self.get_edge(vertex_to, vertex_from):                            
                            e = Edge(vertex_from, vertex_to)
                            self.add_edge(e)
        else:
            print("Violates handshaking lemma. Cannot make Graph with regular edges")
                                                            
                                                                                      
class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""

from random import random
class RandomGraph(Graph):
    def add_random_edges(self, p=0.05):
        vs = self.vertices()
        for i, v in enumerate(vs):
            for j, w in enumerate(vs):
                if j <= i:
                    if random() > p:
                        self.add_edge(Edge(v,w))
class Queue:
    def __init__(self):
        self.bag =[]
    def enqueue(self, obj):
        self.bag.append(obj)
    def dequeue(self):
        removed = self.bag[0]
        self.bag = self.bag[1:]
        return removed
    def isEmpty(self):
        if len(self.bag)==0:
            return True
        else:
            return False
    
def BFS(G, v):
    seen = set()
    Q = Queue()
    Q.enqueue(v)
    while not Q.isEmpty():
        marked = Q.dequeue()
        seen.add(marked)
        neighbors = G.out_vertices(marked)
        for neighbor in neighbors:
            if neighbor not in seen:
                Q.enqueue(neighbor)
    return list(seen)
        
v = Vertex('v')
w = Vertex('w')
v1= Vertex('v1')
v2 = Vertex('v2')
v3 = Vertex('v3')
v4 = Vertex('v4')
v5 = Vertex('v5')
j = [v,w,v1,v2,v3,v4,v5]  
r = RandomGraph(j)
r.add_random_edges(.8)
r.edges()
BFS(r,v)

 
    
def main(script, *args):
    v = Vertex('v')
    print v
    w = Vertex('w')
    print w
    e = Edge(v, w)
    print e
    g = Graph([v,w], [e])
    print g


if __name__ == '__main__':
    import sys
    main(*sys.argv)

