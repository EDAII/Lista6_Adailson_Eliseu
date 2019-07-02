import random, time
from graph import Graph

number = 1
g = Graph()

def generate_graph():
    g.addEdge(0,1)
    i = 1
    for i in range(1,15):
        k = random.randrange(1,15)
        print("g.addEdge(" + str(k) + "," + str(i)+")")
        print("g.addEdge(" + str(i) + "," + str(k)+")")
        g.addEdge(k,i)
        g.addEdge(i,k)
    start = time.time()
    print(g.BFS(0))
    end = time.time()
    diff = float(end - start)
    diff = diff * 1000
    print(diff)
    start = time.time()
    print(g.DFS(0))
    end = time.time()
    diff = float(end - start)
    diff = diff * 1000
    print(diff)
    
while(number):
    print("Escolha uma das opções:\n"
        +"1- Gerar grafo randômico\n"
        +"2- Criar novo grafo\n")
    number = int(input())
    if number == 1:
        generate_graph()
        print("Escolha uma das opções:\n"
        +"1- Percorrer grafo (BFS)\n"
        +"2- Percorrer grafo (DFS)\n"
        +"3- Analizar ciclo ímpar\n"
        +"4- Definir menor caminho entre s e t")
        choice = int(input())
