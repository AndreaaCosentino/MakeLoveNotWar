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
jap = df[df['Country Name'] == "Japan"]
usa = df[df['Country Name'] == "United States"]
rus = df[df['Country Name'] == "Russian Federation"]
chi = df[df['Country Name'] == "China"]
ind = df[df['Country Name'] == "India"]

world_exp = []
jap_exp = []
usa_exp = []
rus_exp = []
chi_exp = []
ind_exp = []
zero_points = []

for (index, colname) in enumerate(df):

    if type(jap.iloc[0][colname]) == np.float64:
        all_years.append(colname)
        avg_this_year = (df[colname].mean() / 1000000000)
        world_exp.append(avg_this_year)
        jap_exp.append((jap.iloc[0][colname] / 1000000000) - avg_this_year)
        usa_exp.append((usa.iloc[0][colname] / 1000000000) - avg_this_year)
        rus_exp.append((rus.iloc[0][colname] / 1000000000) - avg_this_year)
        chi_exp.append((chi.iloc[0][colname] / 1000000000) - avg_this_year)
        ind_exp.append((ind.iloc[0][colname] / 1000000000) - avg_this_year)
        zero_points.append(0)

np_zero = np.array(zero_points)

ax[0].fill_between(all_years, usa_exp, zero_points, where = np.array(usa_exp) >= np_zero, color = '#BFE7F1', label = "Spesa superiore alla media")
ax[0].fill_between(all_years, usa_exp, zero_points, where = np.array(usa_exp) < np_zero, color = '#DD8D81', label = "Spesa inferiore alla media")
ax[0].set_title("Stati Uniti", fontsize = 10)
ax[0].legend(loc = 'upper left')

ax[1].fill_between(all_years, rus_exp, zero_points, where = np.array(rus_exp) >= np_zero, color = '#BFE7F1')
ax[1].fill_between(all_years, rus_exp, zero_points, where = np.array(rus_exp) < np_zero, color = '#DD8D81')
ax[1].set_title("Russia", fontsize = 10)

ax[2].fill_between(all_years, chi_exp, zero_points, where = np.array(chi_exp) >= np_zero, color = '#BFE7F1')
ax[2].fill_between(all_years, chi_exp, zero_points, where = np.array(chi_exp) < np_zero, color = '#DD8D81')
ax[2].set_title("Cina", fontsize = 10)

ax[3].fill_between(all_years, jap_exp, zero_points, where = np.array(jap_exp) >= np_zero, color = '#BFE7F1')
ax[3].fill_between(all_years, jap_exp, zero_points, where = np.array(jap_exp) < np_zero, color = '#DD8D81')
ax[3].set_title("Giappone", fontsize = 10)

ax[4].fill_between(all_years, ind_exp, zero_points, where = np.array(ind_exp) >= np_zero, color = '#BFE7F1')
ax[4].fill_between(all_years, ind_exp, zero_points, where = np.array(ind_exp) < np_zero, color = '#DD8D81')
ax[4].set_title("India", fontsize = 10)
ax[4].set_xticks(["1960", "1980","2000", "2020"])

plt.show()
