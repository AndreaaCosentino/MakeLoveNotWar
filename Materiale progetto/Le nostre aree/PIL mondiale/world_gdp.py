import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("world-gdp-over-the-last-two-millennia.csv")

fig, ax = plt.subplots()

fig.set_size_inches(10, 7)

ax.set_adjustable(adjustable = 'box', share ='True')

ax.set_title("Crescita del PIL mondiale")
ax.set_xlabel("Anno")
ax.set_ylabel("PIL mondiale in miliardi di USD$")

all_years = []
world_gdp = []

for year in df.groupby('Year'):
    current_year = year[0]
    if current_year < 1955:
        continue
    df_year = df[df['Year'] == current_year]

    all_years.append(current_year)

    gdp = df_year['World GDP in 2011 Int.$ (OWID based on World Bank & Maddison (2017))'].mean()

    gdp = gdp / 1000000000

    world_gdp.append(gdp)

ax.fill_between(all_years, world_gdp, alpha = 0.5, color = '#BFE7F1')
ax.plot(all_years, world_gdp, lw = 1.5, color = '#BFE7F1')

plt.show()
