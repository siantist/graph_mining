mat = np.random.random((50,50))
plt.imshow(mat)
plt.colorbar()
plt.show()

import seaborn as sns
%matplotlib inline
sns.heatmap(mat)
