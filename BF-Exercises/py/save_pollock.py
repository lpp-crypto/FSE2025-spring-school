def save_pollock(mat,
                 color_scheme="CMRmap_r",
                 file_name="pollock",
                 vmin=0,
                 vmax=20,
                 folder=None,
                 frame=True,
                 visible_axes=True,
                 colorbar=True,
                 file_type="png"):
    import matplotlib.pyplot as plt
    fig, p = plt.subplots(figsize=(15,15))
    if isinstance(mat, list):
        abs_mat = [[abs(mat[i][j]) for j in xrange(0, len(mat[0]))]
                   for i in xrange(0, len(mat))]
    else:
        abs_mat = [[abs(mat[i][j]) for j in xrange(0, mat.ncols())]
                   for i in xrange(0, mat.nrows())]
    axes = p.imshow(
        abs_mat,
        interpolation="none",
        cmap=plt.cm.get_cmap(color_scheme, 100),
        vmin=vmin,
        vmax=vmax,
    )
    if colorbar:
        fig.colorbar(axes, orientation='vertical', fraction=0.046, pad=0.04)
    p.set_aspect('equal')
    p.get_xaxis().set_visible(visible_axes)
    p.get_yaxis().set_visible(visible_axes)
    p.patch.set_alpha(0)
    p.set_frame_on(frame)
    if folder == None:
        name_base = "{}."+file_type
    else:
        name_base = folder + "/{}." + file_type
    fig.savefig(name_base.format(file_name))
