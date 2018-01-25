def question3(G):
	vertices = G.keys()
	edges = set()
	  for i in vertices:
	     for j in G[i]:
	        if i > j[0]:
	          edges.add((j[1], j[0], i))
	        elif i < j[0]:
	          edges.add((j[1], i, j[0]))
	# sort edges
	    edges = sorted(list(edges))

	    output_edges = []
	    vertices = [set(i) for i in vertices]
	    for i in edges:
	
	        for j in xrange(len(vertices)):
	            if i[1] in vertices[j]:
	                i1 = j
	                 if i[2] in vertices[j]:
 	                i2 = j

	        if i1 < i2:
	            vertices[i1] = set.union(vertices[i1], vertices[i2])
	            vertices.pop(i2)
	            output_edges.append(i)
	        if i1 > i2:
	            vertices[i2] = set.union(vertices[i1], vertices[i2])
	            vertices.pop(i1)
	            output_edges.append(i)

	        if len(vertices) == 1:
	            break
	
    output_graph = {}
	    for i in output_edges:
	        if i[1] in output_graph:
	            output_graph[i[1]].append((i[2], i[0]))
	        else:
	            output_graph[i[1]] = [(i[2], i[0])]
	

	        if i[2] in output_graph:
	            output_graph[i[2]].append((i[1], i[0]))
	        else:
	            output_graph[i[2]] = [(i[1], i[0])]
	     
     return output_graph
	            
	

	def test():
	    G = {'A': [('B', 2)],
	         'B': [('A', 2), ('C', 5)],
	           'C': [('B', 5)]}
	    print "\nTesting"
