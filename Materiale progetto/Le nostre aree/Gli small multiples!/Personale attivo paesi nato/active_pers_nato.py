import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("API_MS.MIL.TOTL.P1_DS2_en_csv_v2_4689881.csv")

fig, ax = plt.subplots(5, 1, sharex = True, sharey = True, layout = "constrained")

fig.set_size_inches(11,7)

plt.suptitle("Numero personale militare (migliaia) (dal 1989 ad oggi)", fontsize = 20)

all_years = []

usa = df[df['Country Name'] == "United States"]
it = df[df['Country Name'] == "Italy"]
uk = df[df['Country Name'] == "United Kingdom"]
ger = df[df['Country Name'] == "Germany"]
fra = df[df['Country Name'] == "France"]

world_avg = []
zero_points = []
usa_n = []
it_n = []
uk_n = []
ger_n = []
fra_n = []

for (index, colname) in enumerate(df):
    if type(usa.iloc[0][colname]) == np.float64:
        if (usa.iloc[0][colname]) >= 1989:
            all_years.append(colname)
            avg_this_year = (df[colname].mean()) / 1000
            world_avg.append(avg_this_year)
            usa_n.append(usa.iloc[0][colname] / 1000)
            it_n.append(it.iloc[0][colname] / 1000)
            uk_n.append(uk.iloc[0][colname] / 1000)
            ger_n.append(ger.iloc[0][colname] / 1000)
            fra_n.append(fra.iloc[0][colname] / 1000)

ax[0].plot(all_years, usa_n, lw = 1.5, color = '#BFE7F1')
ax[0].fill_between(all_years, usa_n, alpha = 0.5, color = '#BFE7F1')
ax[0].plot(all_years, world_avg, lw = 1.5, color = '#DD8D81', label = "Media mondiale")
ax[0].set_title("Stati Uniti", fontsize = 10)
ax[0].legend(loc = 'upper right')

ax[1].plot(all_years, fra_n, lw = 1.5, color = '#BFE7F1')
ax[1].fill_between(all_years, fra_n, alpha = 0.5, color = '#BFE7F1')
ax[1].plot(all_years, world_avg, lw = 1.5, color = '#DD8D81')
ax[1].set_title("Francia", fontsize = 10)

ax[2].plot(all_years, uk_n, lw = 1.5, color = '#BFE7F1')
ax[2].fill_between(all_years, uk_n, alpha = 0.5, color = '#BFE7F1')
ax[2].plot(all_years, world_avg, lw = 1.5, color = '#DD8D81')
ax[2].set_title("Regno Unito", fontsize = 10)

ax[3].plot(all_years, it_n, lw = 1.5, color = '#BFE7F1')
ax[3].fill_between(all_years, it_n, alpha = 0.5, color = '#BFE7F1')
ax[3].plot(all_years, world_avg, lw = 1.5, color = '#DD8D81')
ax[3].set_title("Italia", fontsize = 10)

ax[4].plot(all_years, ger_n, lw = 1.5, color = '#BFE7F1')
ax[4].fill_between(all_years, ger_n, alpha = 0.5, color = '#BFE7F1')
ax[4].plot(all_years, world_avg, lw = 1.5, color = '#DD8D81')
ax[4].set_title("Germania", fontsize = 10)

ax[4].set_xticks(["1990", "2000", "2010", "2020"])
plt.show()
