import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("military-expenditure-as-a-share-of-gdp.csv")

fig, ax = plt.subplots(5, 1, sharex = True, sharey = True, layout = "constrained")
plt.ylim(-100, 200)
ax[0].set_yticks([0])
fig.set_size_inches(11,7)
#plt.suptitle("Quali stati investono di più in spese militari? (% rispetto al PIL)", fontsize = 20)
avg_world_exp = []
all_years = []


usa = df[df['Entity'] == "United States"]
chi = df[df['Entity'] == "China"]
jap = df[df['Entity'] == "Japan"]
ind = df[df['Entity'] == "India"]
rus = df[df['Entity'] == "Russia"]


average_exp = []
usa_diff = []
chi_diff = []
jap_diff = []
ind_diff = []
rus_diff = []

zero_points = []

for year in df.groupby('Year'):
    current_year = year[0]

    if current_year < 1900:
        continue
    df_year = df[df['Year'] == current_year]

    all_years.append(current_year)

    avg = df_year['Military expenditure as a share of GDP'].mean()

    average_exp.append(avg)

    usa_diff.append(usa[usa['Year'] == current_year]['Military expenditure as a share of GDP'].mean() - avg)
    chi_diff.append(chi[chi['Year'] == current_year]['Military expenditure as a share of GDP'].mean() - avg)
    jap_diff.append(jap[jap['Year'] == current_year]['Military expenditure as a share of GDP'].mean() - avg)
    ind_diff.append(ind[ind['Year'] == current_year]['Military expenditure as a share of GDP'].mean() - avg)
    rus_diff.append(rus[rus['Year'] == current_year]['Military expenditure as a share of GDP'].mean() - avg)

    zero_points.append(0)

np_zero = np.array(zero_points)

ax[0].fill_between(all_years, usa_diff, zero_points, where = np.array(usa_diff) >= np_zero, color = '#BFE7F1', label = "Spesa superiore alla media")
ax[0].fill_between(all_years, usa_diff, zero_points, where = np.array(usa_diff) < np_zero, color = '#DD8D81', label = "Spesa inferiore alla media")
ax[0].set_title("Stati Uniti", fontsize = 10)
ax[0].legend(loc = 'upper right')

ax[1].fill_between(all_years, rus_diff, zero_points, where = np.array(rus_diff) >= np_zero, color = '#BFE7F1')
ax[1].fill_between(all_years, rus_diff, zero_points, where = np.array(rus_diff) < np_zero, color = '#DD8D81')
ax[1].set_title("Russia", fontsize = 10)

ax[2].fill_between(all_years, chi_diff, zero_points, where = np.array(chi_diff) >= np_zero, color = '#BFE7F1')
ax[2].fill_between(all_years, chi_diff, zero_points, where = np.array(chi_diff) < np_zero, color = '#DD8D81')
ax[2].set_title("Cina", fontsize = 10)

ax[3].fill_between(all_years, jap_diff, zero_points, where = np.array(jap_diff) >= np_zero, color = '#BFE7F1')
ax[3].fill_between(all_years, jap_diff, zero_points, where = np.array(jap_diff) < np_zero, color = '#DD8D81')
ax[3].set_title("Giappone", fontsize = 10)

ax[4].fill_between(all_years, ind_diff, zero_points, where = np.array(ind_diff) >= np_zero, color = '#BFE7F1')
ax[4].fill_between(all_years, ind_diff, zero_points, where = np.array(ind_diff) < np_zero, color = '#DD8D81')
ax[4].set_title("India", fontsize = 10)

plt.show()
