def top_loss(top_indices, gi, gj, loss_fn):
  loss_val = loss_fn(top_indices[gi], top_indices[gj])
  return loss_val
