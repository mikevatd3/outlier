import pandas as pd
import numpy as np
from scipy.stats import lognorm
from sklearn.mixture import GaussianMixture
import seaborn as sn
import matplotlib.pyplot as plt

CLIP = 25


def log_assessed_val(vals):
    return np.log10(np.sum(vals))


df = pd.read_parquet("temp_parcels.gzip")

addresses = df.groupby(["clean_address"]).agg(
    num_parcels=("clean_address", "count"),
    log_assessed_val=("assessed_value", log_assessed_val),
)

"""
addresses_by_class = df.groupby(["clean_address", "super_class"]).agg(
    num_parcels=("clean_address", "count"),
    log_assessed_val=("assessed_value", log_assessed_val)
)

addresses_by_empty = df.groupby(["clean_address", "empty_lot"]).agg(
    num_parcels=("clean_address", "count"),
    log_assessed_val=("assessed_value", log_assessed_val)
)
"""

gmm = GaussianMixture(n_components=3, covariance_type="full")
gmm.fit(addresses[["log_assessed_val"]])

print(f"Model Weights: {gmm.weights_}")
print(f"Model Means: {gmm.means_.flatten()}")
print(f"Model covariances: {gmm.covariances_.flatten()}")
print(f"Model aic: {gmm.aic(addresses[['log_assessed_val']])}")
print(f"Model bic: {gmm.bic(addresses[['log_assessed_val']])}")

ax = sn.kdeplot(gmm.sample(1000)[0], label="Model output")
ax = sn.kdeplot(
    addresses["log_assessed_val"].sample(1000), ax=ax, label="True distribution"
)
plt.legend()
plt.show()


"""
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

sample = addresses.sort_values("log_assessed_val")[CLIP:-CLIP].sample(5000) 

sn.kdeplot(
    sample,
    x="log_assessed_val",
    y="num_parcels",
    ax=ax1,
)
ax1.set_ylim(0, 7)


sample = addresses_by_class.sort_values("log_assessed_val")[CLIP:-CLIP].sample(5000) 

sn.histplot(
    sample,
    x="log_assessed_val",
    multiple="stack",
    hue="super_class",
    ax=ax2,
)

sample = addresses_by_empty.sort_values("log_assessed_val")[CLIP:-CLIP].sample(5000) 

sn.histplot(
    sample,
    x="log_assessed_val",
    multiple="stack",
    hue="empty_lot",
    ax=ax3,
    kde=True,
)

plt.show()
"""
