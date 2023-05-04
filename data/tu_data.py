#https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html#torch_geometric.datasets.TUDataset
from torch_geometric.datasets import TUDataset
tu_data = TUDataset(root="tutorial1",name= "ENZYMES")
# https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.data.Data.html#torch_geometric.data.Data
t1 = tu_data[1]
t1.x
