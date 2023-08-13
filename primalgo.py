#création et le dessin du graphe
import networkx as nx

#l'affichage graphiques
import matplotlib.pyplot as plt

#Gestion de la file de priorité
from heapq import heappop, heappush, heapify

def prim_algorithm(graph, Debut):
    # Initialisation
    ArbreMinimal = {}
    NoeudVisite = [Debut]
    Arete = []

    for Destination, Poids in graph[Debut].items():
        
        Arete.append((Poids, Debut, Destination))
    heapify(Arete)
    print(f"Sommets voisin au sommet de départ : {Arete}")
    # Comparaison entre les eléments d'une liste en fontion du poids

    #Tant que la liste n'est pas vide
    while Arete:
        # Récupération de l'arête de poids minimal
        Poids, Deb, Destination =  heappop(Arete)
        
        #Si le noeud de destination n'est pas visité
        if Destination not in NoeudVisite:
            NoeudVisite.append(Destination)
            # Ajout de l'arête dans l'arbre couvrant minimal
            ArbreMinimal[(Deb, Destination)] = Poids

            # Ajout des nouvelles arêtes à la file de priorité
            for Destination_next, Poids in graph[Destination].items():
                if Destination_next not in NoeudVisite:
                       heappush(Arete, (Poids, Destination, Destination_next))

    return ArbreMinimal


graph = {
    'A': {'B': 2, 'G': 5},
    'B': {'A': 2 ,'G': 15, 'D': 10,'E': 3},
    'C': {'G': 5, 'D': 7, 'E':10, 'F':12},
    'D': {'B': 10, 'E': 1, 'G': 3, 'C': 7},
    'E': {'B': 3, 'C': 10, 'D': 1, 'F': 11},
    'F': {'C': 12, 'E': 11},
    'G': {'A': 5, 'B': 15, 'C':5, 'D':3}
}

# Algorithme de Prim
ArbreMinimal = prim_algorithm(graph, 'D')
print("Arbre couvrant minimal :", ArbreMinimal)

# Création du graphe initial avec NetworkX
G = nx.Graph()
for debut, voisins in graph.items():
    for destination, poids in voisins.items():
        G.add_edge(debut, destination, weight=poids)

# Dessin du graphe initial
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, with_labels=True)

# Dessin de l'arbre couvrant minimal
ArbreMinimal_edges = [(Debut, Destination) for Debut, Destination in ArbreMinimal]
nx.draw_networkx_edges(G, pos=pos, edgelist=ArbreMinimal_edges, edge_color='r')

# Affichage du graphique final
plt.axis('off')
plt.show()