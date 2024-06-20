import numpy as np
import seaborn as sn
from scipy.stats import lognorm
import pandas as pd
import matplotlib.pyplot as plt

# 1022298048 actual
# 1028335885 modeled


# ---- static parameters

NUM_OWNERS = 10000


# ---- adjustable parameters

fraction_splits = 5
split_times = 10


"""
1. Just pick some number of investors who might split their
investment into multiple llcs. DONE

2. Pick the investors based on their current size, assuming
that investors with more value held are more likely to split 
that value among. NEXT

3. Include the number of LLCs that the landlord splits as a 
function of the size of the investment.
"""


df = pd.read_parquet("temp_parcels.gzip")
investors = df.groupby("clean_taxpayer").agg({"assessed_value": "sum"})
addresses = df.groupby("clean_address").agg({"assessed_value": "sum"})

sigma, loc, scale = lognorm.fit(investors["assessed_value"])

owners = np.round(lognorm.rvs(sigma, loc=loc, scale=scale, size=(NUM_OWNERS)))

print(owners)

# chance = np.log(owners)
# scale = chance - np.min(chance)
# scale = scale / scale.sum()


"""
indicies = np.random.choice(
    np.arange(owners.shape[0]), 
    size=(NUM_OWNERS // fraction_splits), 
    p=scale,
    replace=False
)

mask = np.ones(owners.shape[0], dtype=bool)
mask[indicies] = False

leaves = owners[mask]
splits = owners[indicies]

new_owners = np.concatenate([
    leaves, 
    *[
        (splits / split_times)
        for _ in range(split_times)
    ]
])


# ax = sn.histplot(new_owners, log_scale=True, ax=ax, label="disguised")
ax = sn.histplot(
    investors.sample(10000)["assessed_value"].rename("investors"),
    log_scale=True,
    legend=True,
    ax=ax
)
"""
ax = sn.histplot(owners, log_scale=True, label="underlying")
ax = sn.histplot(
    addresses.sample(10000)["assessed_value"].rename("addresses"),
    ax=ax,
    log_scale=True,
    legend=True,
)
plt.show()

