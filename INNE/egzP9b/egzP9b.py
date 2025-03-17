from egzP9btesty import runtests

def dyrektor( G, R ):
	#Tutaj proszę wpisać własną implementację 
	def DFS_Visit(G,u):
		nonlocal cycle
		visited[u] = True
		for v in G[u]:
			G[u].remove(v)
			DFS_Visit(G,v)
		cycle = [u] + cycle

	n = len(G)
	visited = [False for _ in range(n)]
	cycle = []

	for i in range(n):
		for j in range(len(R[i])):
			G[i].remove(R[i][j])

	DFS_Visit(G,0)

	return cycle
	
runtests(dyrektor, all_tests=True)
