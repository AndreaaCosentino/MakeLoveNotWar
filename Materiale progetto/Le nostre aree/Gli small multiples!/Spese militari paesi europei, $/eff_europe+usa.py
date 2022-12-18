import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("API_MS.MIL.XPND.CD_DS2_en_csv_v2_4694395.csv")

fig, ax = plt.subplots(5, 1, sharex = True, sharey = True, layout = "constrained")
fig.set_size_inches(11,7)
plt.ylim(-100, 750)

ax[0].set_yticks([0])
plt.suptitle("Quali stati investono di più in spese militari? (Spesa effettiva in miliardi USD$)", fontsize = 20)

all_years = []
usa = df[df['Country Name'] == "United States"]
it = df[df['Country Name'] == "Italy"]
uk = df[df['Country Name'] == "United Kingdom"]
ger = df[df['Country Name'] == "Germany"]
fra = df[df['Country Name'] == "France"]
ukr = df[df['Country Name'] == "Ukraine"]

world_exp = []
usa_exp = []
uk_exp = []
it_exp = []
ger_exp = []
fra_exp = []
ukr_exp = []
zero_points = []

for (index, colname) in enumerate(df):

    if type(usa.iloc[0][colname]) == np.float64:
        all_years.append(colname)
        avg_this_year = (df[colname].mean() / 1000000000)
        world_exp.append(avg_this_year)
        usa_exp.append((usa.iloc[0][colname] / 1000000000) - avg_this_year)
        uk_exp.append((uk.iloc[0][colname] / 1000000000) - avg_this_year)
        it_exp.append((it.iloc[0][colname] / 1000000000) - avg_this_year)
        ger_exp.append((ger.iloc[0][colname] / 1000000000) - avg_this_year)
        fra_exp.append((fra.iloc[0][colname] / 1000000000) - avg_this_year)
        ukr_exp.append((ukr.iloc[0][colname] / 1000000000) - avg_this_year)
        zero_points.append(0)

np_zero = np.array(zero_points)

ax[0].fill_between(all_years, usa_exp, zero_points, where = np.array(usa_exp) >= np_zero, color = '#BFE7F1', label = "Spesa superiore alla media")
ax[0].fill_between(all_years, usa_exp, zero_points, where = np.array(usa_exp) < np_zero, color = '#DD8D81', label = "Spesa inferiore alla media")
ax[0].set_title("Stati Uniti", fontsize = 10)

ax[0].legend(loc = 'upper left')

ax[1].fill_between(all_years, fra_exp, zero_points, where = np.array(fra_exp) >= np_zero, color = '#BFE7F1')
ax[1].fill_between(all_years, fra_exp, zero_points, where = np.array(fra_exp) < np_zero, color = '#DD8D81')
ax[1].set_title("Francia", fontsize = 10)

ax[2].fill_between(all_years, uk_exp, zero_points, where = np.array(uk_exp) >= np_zero, color = '#BFE7F1')
ax[2].fill_between(all_years, uk_exp, zero_points, where = np.array(uk_exp) < np_zero, color = '#DD8D81')
ax[2].set_title("Regno Unito", fontsize = 10)

ax[3].fill_between(all_years, it_exp, zero_points, where = np.array(it_exp) >= np_zero, color = '#BFE7F1')
ax[3].fill_between(all_years, it_exp, zero_points, where = np.array(it_exp) < np_zero, color = '#DD8D81')
ax[3].set_title("Italia", fontsize = 10)

ax[4].fill_between(all_years, ger_exp, zero_points, where = np.array(ger_exp) >= np_zero, color = '#BFE7F1')
ax[4].fill_between(all_years, ger_exp, zero_points, where = np.array(ger_exp) < np_zero, color = '#DD8D81')
ax[4].set_title("Germania", fontsize = 10)
ax[4].set_xticks(["1960", "1980","2000", "2020"])

plt.show()
