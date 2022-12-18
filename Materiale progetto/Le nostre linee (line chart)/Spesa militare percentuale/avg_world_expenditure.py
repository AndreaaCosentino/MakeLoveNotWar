import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("military-expenditure-as-a-share-of-gdp.csv")

fig, ax = plt.subplots()

fig.set_facecolor('#fac86a')
fig.set_size_inches(10, 7)

ax.spines['bottom'].set_color('#004249')
ax.spines['top'].set_color('#004249')
ax.spines['right'].set_color('#004249')
ax.spines['left'].set_color('#004249')
ax.xaxis.label.set_color('#004249')
ax.tick_params(axis='x', colors='#004249')
ax.yaxis.label.set_color('#004249')
ax.tick_params(axis='y', colors='#004249')
ax.title.set_color('#004249')

ax.set_facecolor('#fac86a')
ax.set_adjustable(adjustable = 'box', share ='True')

#ax.set_title("Average military expenditure in all world since 1827 to 2016 as a share of GDP")
ax.set_xlabel("Anno")
ax.set_ylabel("Spesa militare rapportata al pil, in %")

avg_world_exp = []
all_years = []

for year in df.groupby('Year'):
    current_year = year[0]
    df_year = df[df['Year'] == current_year]

    all_years.append(current_year)

    average_exp = df_year['Military expenditure as a share of GDP'].mean()

    avg_world_exp.append(average_exp)



ax.plot(all_years, avg_world_exp, color = '#0097a7')

plt.show()
