import useful
import networkx as nx
import matplotlib.pyplot as plt
file = useful.openFile(11)

maps = {}
for line in file:
    inp = line.split(":")[0]
    out = line.split(":")[1].split(" ")[1:]
    maps[inp] = out
maps["out"] = []

memo = {}
def dist(stri, goal):
    if (stri,goal) in memo:
        return memo[(stri,goal)]
    else:
        if goal in maps[stri]:
            return 1
        # print("got")
        a = sum(dist(a, goal) for a in maps[stri])
        memo[(stri,goal)] = a
        return a

print(dist("you", "out"))
print(dist("svr", "fft")*dist("fft","dac")*dist("dac","out") + dist("svr", "dac")*dist("dac","fft")*dist("fft","out"))


G = nx.Graph()
for inp in maps.keys():
    for out in maps[inp]:
        G.add_edge(inp,out)

# me when i visualize
# colors = ['red' if node_name in ["fft","dac","svr","out"] else 'blue' for node_name in list(G.nodes)]
# sizes = [10 if node_name in ["fft","dac","svr","out"] else 1 for node_name in list(G.nodes)]
# pos = nx.spring_layout(G, k=5, iterations=500000)
# nx.draw(G, pos, with_labels=True, node_color=colors, node_size=sizes, edge_color='gray', font_size=10)
# plt.show()