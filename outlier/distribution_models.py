import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sn
import matplotlib.pyplot as plt


df = pd.read_parquet("temp_parcels.gzip")
investors = df.groupby("clean_taxpayer").agg({"assessed_value": "sum"})
addresses = df.groupby("clean_address").agg({"assessed_value": "sum"})

data = addresses["assessed_value"].sort_values()[100:-100]


distributions = {
    "lognorm": stats.lognorm,
    "pareto": stats.pareto,
    "weibull_min": stats.weibull_min,
    "gamma": stats.gamma,
    "expon": stats.expon,
    "genextreme": stats.genextreme,
}

fits = {}
for name, dist in distributions.items():
    params = dist.fit(data)
    fits[name] = params

## Compare goodness of fit
aic_bic = []
for name, params in fits.items():
    dist = distributions[name]
    log_likelihood = np.sum(dist.logpdf(data, *params))
    k = len(params)
    aic = 2 * k - 2 * log_likelihood
    bic = np.log(len(data)) * k - 2 * log_likelihood
    aic_bic.append((name, aic, bic))

aic_bic.sort(key=lambda x: x[1])  # Sort by AIC

print("Distribution comparison (sorted by AIC):")
for name, aic, bic in aic_bic:
    print(f"{name}: AIC={aic}, BIC={bic}")


# Plot the best fit
best_fit_name = aic_bic[0][0]
best_fit_params = fits[best_fit_name]

model_vals = distributions[best_fit_name].rvs(*best_fit_params, size=5000)
sn.histplot(model_vals, log_scale=True)
sn.histplot(data.sample(5000), log_scale=True)
plt.legend()
plt.show()
