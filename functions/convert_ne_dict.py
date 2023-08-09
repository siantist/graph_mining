def convert_ne_dict(data, out_ne):
  a = to_dense_adj(data.edge_index)
  an = np.array(a[0])
  anp = an.astype(np.float)
  ne_array = out_ne.detach().numpy()
  ne_dict ={}
  n = len(ne_array)
  for i in range(n):
    ne_dict[i] = ne_array[i]
  return ne_dict, anp
