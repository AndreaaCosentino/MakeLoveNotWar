import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

exp_df = pd.read_csv("military-expenditure-as-a-share-of-gdp.csv")
gdp_df = pd.read_csv("world-gdp-over-the-last-two-millennia.csv")

fig, ax = plt.subplots()

fig.set_size_inches(10, 7)

ax.set_adjustable(adjustable = 'box', share ='True')

ax.set_title("Spesa militare mondiale (in Miliardi di USD$)")
ax.set_xlabel("Anno")
ax.set_ylabel("USD$ (Miliardi)")

world_exp = []
all_years = []

for year in exp_df.groupby('Year'):
    current_year = year[0]
    if current_year < 1955:
        continue
    df_year = exp_df[exp_df['Year'] == current_year]

    gdp_year_df = gdp_df[gdp_df['Year'] == current_year]

    average_exp = df_year['Military expenditure as a share of GDP'].mean()
    gdp = gdp_year_df['World GDP in 2011 Int.$ (OWID based on World Bank & Maddison (2017))'].mean()
    gdp = gdp / 1000000000
    exp = gdp * (average_exp / 100)

    if exp >= 0:
        world_exp.append(exp)
        all_years.append(current_year)



ax.fill_between(all_years, world_exp, alpha = 0.5, color = '#BFE7F1')
ax.plot(all_years, world_exp, lw = 1.5, color = '#BFE7F1')
plt.show()
