def run_kernel(g1, g2):
    from grakel.kernels import PropagationAttr
    pak = PropagationAttr(normalize=True, verbose=False)
    pak.fit_transform([g1])
    sc = pak.transform([g2])

    return sc
