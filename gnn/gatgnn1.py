import torch
from torch import Tensor
from torch.nn import Sequential, Linear, ReLU
#from torch.nn import GATConv
from torch_geometric.nn.conv import GATConv
from torch_geometric.nn.conv import MessagePassing

class gatgnn1(MessagePassing):
  def __init__(self, in_channels, out_channels): # ,W
      super().__init__(aggr="mean") # mean or max aggregation ?
      self.mlp = Sequential(
          Linear(2*in_channels, out_channels),#, weight_initializer=W),#, bias_initializer=b),
          GATConv(out_channels, out_channels) # gatconv forward( return_attention_weights = True)
      )
  def forward(self, x:Tensor, edge_index:Tensor) -> Tensor:
      return self.propogate(edge_index, x=x)
  def message(self, x_j:Tensor, x_i:Tensor) -> Tensor:
      # x_j source node shape [num_edges, in_channels], x_i target node same shape
      edge_features = torch.cat([x_i, x_j - x_i], dim=-1)
      return self.mlp(edge_features)
  def get_node_embedding(self):
      return self.x
  def get_edge_embedding(self):
      return self.edge_index, self.attention_weights
