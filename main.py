from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os, random, time
from graph import Graph

number = 1
values = []
n=0
try:
    g = Graph()
except:
    print('Exception occurred')

def comparation_graph(result_search,n):
    plt.ylabel('Tempo para %d nós (em milisegundos)' % (n))
    
    for key in result_search.keys():
        plt.bar(key, result_search[key])

    plt.show()

def search_results(n, key):
    g.addEdge(0,1)
    i = 1
    for i in range(1,n):
        k = random.randrange(1,n)
        # print("g.addEdge(" + str(k) + "," + str(i)+")")
        # print("g.addEdge(" + str(i) + "," + str(k)+")")
        g.addEdge(k,i)
        g.addEdge(i,k)
    if(key == "BFS"):
        return g.BFS(0)
    else:
        return g.DFS(0)

results_search = {'BFS': [], 'DFS': []}
result_search = {'BFS': 0, 'DFS': 0}

while(number):
    start = 0
    end = 0
    value = 0
    values.clear
    value_sought = 0
    diff = 0
    i = 0
    print("Escolha uma das opções:\n"
        +"1- Comparativo de busca BFS x DFS (busca valor randômico em valores para n nós)\n"
        +"0- Para sair\n")
    number = int(input())
    if number == 1 or number == 2 or number == 3:
        print("Digite a quantidade de nós:")
        n = int(input())
        if number == 1:
            print("Digite quantas iterações você deseja buscar para %d nós:" % n)
            b = int(input())
        for key in result_search.keys():
            if key == 'DFS': 
                g = Graph()
                result_dfs = None
                if number == 1:
                    start = time.time()
                    for i in range(0,b):
                        result_dfs = search_results(n,key)
                elif number == 2:
                    start = time.time()
                    for i in range(0,b):
                        result_dfs = search_results(n,key)
                else:
                    start = time.time()
                    for i in range(0,b):
                        result_dfs = search_results(n,key)

            elif key == 'BFS':
                if number == 1:
                    start = time.time()
                    for i in range(0,b):
                        result_bfs = search_results(n,key)
                elif number == 2:
                    start = time.time()
                    for i in range(0,b):
                        result_bfs = search_results(n,key)
                else:
                    start = time.time()
                    for i in range(0,b):
                        result_bfs = search_results(n,key)

            end = time.time()
            diff = float(end - start)
            diff = diff * 1000
            
            if number == 1:
                result_search[key] = diff
                results_search[key].append(diff)

        if number == 1:
            comparation_graph(result_search, n)

    print("Aperte enter para continuar!")
    input()
    os.system('clear')