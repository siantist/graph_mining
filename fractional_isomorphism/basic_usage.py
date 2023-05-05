# https://github.com/jfinkels/fraciso
from networkx import Graph
from fraciso import are_fractionally_isomorphic

# Create a NetworkX Graph objects G and H.
#G = ...
#H = ...

print('G is fractionally isom. to H?', are_fractionally_isomorphic(G, H))
