import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("API_MS.MIL.TOTL.P1_DS2_en_csv_v2_4689881.csv")

fig, ax = plt.subplots(5, 1, sharex = True, sharey = True, layout = "constrained")

fig.set_size_inches(11,7)

plt.suptitle("Numero personale militare (migliaia) (dal 1989 ad oggi)", fontsize = 20)

all_years = []

usa = df[df['Country Name'] == "United States"]
rus = df[df['Country Name'] == "Russian Federation"]
chi = df[df['Country Name'] == "China"]
jap = df[df['Country Name'] == "Japan"]
ind = df[df['Country Name'] == "India"]

world_avg = []
zero_points = []
usa_n = []
rus_n = []
chi_n = []
jap_n = []
ind_n = []

for (index, colname) in enumerate(df):
    if type(usa.iloc[0][colname]) == np.float64:
        if (usa.iloc[0][colname]) >= 1989:
            all_years.append(colname)
            avg_this_year = (df[colname].mean()) / 1000
            world_avg.append(avg_this_year)
            usa_n.append(usa.iloc[0][colname] / 1000)
            rus_n.append(rus.iloc[0][colname] / 1000)
            chi_n.append(chi.iloc[0][colname] / 1000)
            jap_n.append(jap.iloc[0][colname] / 1000)
            ind_n.append(ind.iloc[0][colname] / 1000)

ax[0].plot(all_years, usa_n, lw = 1.5, color = '#BFE7F1')
ax[0].fill_between(all_years, usa_n, alpha = 0.5, color = '#BFE7F1')
ax[0].plot(all_years, world_avg, lw = 1.5, color = '#DD8D81', label = "Media mondiale")
ax[0].set_title("Stati Uniti", fontsize = 10)
ax[0].legend(loc = 'upper right')

ax[1].plot(all_years, rus_n, lw = 1.5, color = '#BFE7F1')
ax[1].fill_between(all_years, rus_n, alpha = 0.5, color = '#BFE7F1')
ax[1].plot(all_years, world_avg, lw = 1.5, color = '#DD8D81')
ax[1].set_title("Russia", fontsize = 10)

ax[2].plot(all_years, chi_n, lw = 1.5, color = '#BFE7F1')
ax[2].fill_between(all_years, chi_n, alpha = 0.5, color = '#BFE7F1')
ax[2].plot(all_years, world_avg, lw = 1.5, color = '#DD8D81')
ax[2].set_title("Cina", fontsize = 10)

ax[3].plot(all_years, jap_n, lw = 1.5, color = '#BFE7F1')
ax[3].fill_between(all_years, jap_n, alpha = 0.5, color = '#BFE7F1')
ax[3].plot(all_years, world_avg, lw = 1.5, color = '#DD8D81')
ax[3].set_title("Giappone", fontsize = 10)

ax[4].plot(all_years, ind_n, lw = 1.5, color = '#BFE7F1')
ax[4].fill_between(all_years, ind_n, alpha = 0.5, color = '#BFE7F1')
ax[4].plot(all_years, world_avg, lw = 1.5, color = '#DD8D81')
ax[4].set_title("India", fontsize = 10)

ax[4].set_xticks(["1990", "2000", "2010", "2020"])
plt.show()
