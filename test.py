import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt

uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)
plt.show()


bx = sns.heatmap(uniform_data, vmin=0, vmax=1)
plt.show()


normal_data = np.random.randn(10, 12)
cx = sns.heatmap(normal_data, center=0)
plt.show()


flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
dx = sns.heatmap(flights)
plt.show()


ex = sns.heatmap(flights, annot=True, fmt="d")
plt.show()


fx = sns.heatmap(flights, linewidths=.5)
plt.show()


gx = sns.heatmap(flights, cmap="YlGnBu")
plt.show()


hx = sns.heatmap(flights, center=flights.loc["Jan", 1955])
plt.show()


data = np.random.randn(50, 20)
ix = sns.heatmap(data, xticklabels=2, yticklabels=False)
plt.show()


jx = sns.heatmap(flights, cbar=False)
plt.show()


grid_kws = {"height_ratios": (.9, .05), "hspace": .3}
f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)
kx = sns.heatmap(flights, ax=ax,
                 cbar_ax=cbar_ax,
                 cbar_kws={"orientation": "horizontal"})
plt.show()

corr = np.corrcoef(np.random.randn(10, 200))
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    lx = sns.heatmap(corr, mask=mask, vmax=.3, square=True)

plt.show()