import seaborn as sns; sns.set_theme(color_codes=True)
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
species = iris.pop("species")
g = sns.clustermap(iris)
#plt.show()


g = sns.clustermap(iris,
                   figsize=(7, 5),
                   row_cluster=False,
                   dendrogram_ratio=(.1, .2),
                   cbar_pos=(0, .2, .03, .4))
#plt.show()

lut = dict(zip(species.unique(), "rbg"))
row_colors = species.map(lut)
g = sns.clustermap(iris, row_colors=row_colors)


g = sns.clustermap(iris, cmap="mako", vmin=0, vmax=10)

g = sns.clustermap(iris, metric="correlation")

g = sns.clustermap(iris, method="single")

g = sns.clustermap(iris, standard_scale=1)

g = sns.clustermap(iris, z_score=0, cmap="vlag")

plt.show()