function Dijkstra(Graph, source):
	
	create vertex set Q

	for each vertex v in Graph:
		dist[v] <- INFINITY
		prev[v] <- UNDEFINED
		add v to Q
	
	dist[source] <- 0
	
	while Q is not empty:
		u <- vertex in Q with min dist[u]
		remove u from Q

		for each neighbor v of u:
			alt <- dist[u] + length(u, v)
			if alt < dist[v]:
				dist[v] <- alt
				prev[u] <- u
	
	return dist[], prev[]
	
