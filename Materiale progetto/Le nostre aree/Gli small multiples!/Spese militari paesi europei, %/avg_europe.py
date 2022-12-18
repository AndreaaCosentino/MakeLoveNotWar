import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("military-expenditure-as-a-share-of-gdp.csv")

fig, ax = plt.subplots(4, 1, sharex = True, sharey = True, layout = "constrained")
ax[0].set_yticks([0])
plt.ylim(-30,85)
fig.set_size_inches(11,7)
plt.suptitle("Quali stati investono di più in spese militari? (% rispetto al PIL)", fontsize = 20)
avg_world_exp = []
all_years = []



it = df[df['Entity'] == "Italy"]
uk = df[df['Entity'] == "United Kingdom"]
ger = df[df['Entity'] == "Germany"]
west_ger = df[df['Entity'] == "West Germany"]
fra = df[df['Entity'] == "France"]

average_exp = []
usa_diff = []
uk_diff = []
it_diff = []
ger_diff = []
fra_diff = []
rus_diff = []
ukr_diff = []
zero_points = []

for year in df.groupby('Year'):
    current_year = year[0]
    df_year = df[df['Year'] == current_year]

    all_years.append(current_year)

    avg = df_year['Military expenditure as a share of GDP'].mean()

    average_exp.append(avg)

    fra_diff.append(fra[fra['Year'] == current_year]['Military expenditure as a share of GDP'].mean() - avg)
    uk_diff.append(uk[uk['Year'] == current_year]['Military expenditure as a share of GDP'].mean() - avg)
    it_diff.append(it[it['Year'] == current_year]['Military expenditure as a share of GDP'].mean() - avg)
    if current_year >= 1955 and current_year <= 1990:
        ger_diff.append(west_ger[west_ger['Year'] == current_year]['Military expenditure as a share of GDP'].mean() - avg)
    else:
        ger_diff.append(ger[ger['Year'] == current_year]['Military expenditure as a share of GDP'].mean() - avg)


    zero_points.append(0)

np_zero = np.array(zero_points)

ax[0].fill_between(all_years, fra_diff, zero_points, where = np.array(fra_diff) >= np_zero, color = '#BFE7F1', label = "Spesa superiore alla media")
ax[0].fill_between(all_years, fra_diff, zero_points, where = np.array(fra_diff) < np_zero, color = '#DD8D81', label = "Spesa inferiore alla media")
ax[0].set_title("Francia", fontsize = 10)
ax[0].legend(loc = 'upper right')

ax[1].fill_between(all_years, uk_diff, zero_points, where = np.array(uk_diff) >= np_zero, color = '#BFE7F1')
ax[1].fill_between(all_years, uk_diff, zero_points, where = np.array(uk_diff) < np_zero, color = '#DD8D81')
ax[1].set_title("Regno Unito", fontsize = 10)

ax[2].fill_between(all_years, it_diff, zero_points, where = np.array(it_diff) >= np_zero, color = '#BFE7F1')
ax[2].fill_between(all_years, it_diff, zero_points, where = np.array(it_diff) < np_zero, color = '#DD8D81')
ax[2].set_title("Italia", fontsize = 10)

ax[3].fill_between(all_years, ger_diff, zero_points, where = np.array(ger_diff) >= np_zero, color = '#BFE7F1')
ax[3].fill_between(all_years, ger_diff, zero_points, where = np.array(ger_diff) < np_zero, color = '#DD8D81')
ax[3].set_title("Germania", fontsize = 10)

plt.show()
