import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

TEXT_INPUT = './input.txt'
TEXT_TREE = './output_synconst.txt_0.txt'


f = open(TEXT_INPUT, "r")
text_input = f.read()
f.close()

f = open(TEXT_TREE, "r")
text_tree = f.read()
f.close()

G = nx.Graph()

print("_______________________")
print(text_input)
print("_______________________")
print(text_tree)
print("_______________________")


tokens = text_tree.split()
print(tokens)
print("_______________________")

first_node = True
nodes = {}
log = []
for t in tokens:
    print('-----------------------------------------')
    split = t.split(')')
    print(t.split(')'))
    print('>> SPLIT: ', split)    
    print('>> SPLIT[0]: ', split[0])    
    aux = split[0].replace('(','')
    print('>> AUX: ', aux)

    if aux in nodes:
        nodes[aux] = nodes[aux] + 1
    else:
        nodes[aux] = 0
    node_name = aux + '-' + str(nodes[aux])
    # if aux == 'UNK':
    #     continue 
    # node_name = aux
    G.add_node(node_name)
    log.append(node_name)
    if not first_node:
        log_size = len(log)
        print(log)
        print(">> EDGE: (",log[log_size-2],",", node_name, ") |")
        G.add_edge(log[log_size-2], node_name)
    if len(split) > 1:
        print(">> LOG BEFORE: ", log)
        del log[log_size-len(split):log_size]
        print(">> LOG AFTER: ", log)

    first_node = False

#### CODE TO REMOVE UNK NODES ####
# for i in range(0,nodes['UNK']+1):
#     node_unk = 'UNK-'+str(i)
#     edges = G.edges([node_unk]) 
#     edges = list(edges)
#     G.add_edge(edges[0][1],edges[1][1])
#     G.remove_node('UNK-'+str(i))

pos=graphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=True, font_weight='bold')
plt.savefig("./grafo.png")