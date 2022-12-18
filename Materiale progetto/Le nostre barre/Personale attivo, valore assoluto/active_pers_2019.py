import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("API_MS.MIL.TOTL.P1_DS2_en_csv_v2_4689881.csv")

fig, ax = plt.subplots()

fig.set_size_inches(11,7)

#plt.suptitle("Numero personale militare (migliaia) (Anno 2019)", fontsize = 20)

all_years = []

usa = df[df['Country Name'] == "United States"]
it = df[df['Country Name'] == "Italy"]
uk = df[df['Country Name'] == "United Kingdom"]
ger = df[df['Country Name'] == "Germany"]
fra = df[df['Country Name'] == "France"]
rus = df[df['Country Name'] == "Russian Federation"]
chi = df[df['Country Name'] == "China"]
jap = df[df['Country Name'] == "Japan"]
ind = df[df['Country Name'] == "India"]
nk = df[df['Country Name'] == "Korea, Dem. People's Rep."]

world_avg = 0
usa_2019 = 0
it_2019 = 0
uk_2019 = 0
ger_2019 = 0
fra_2019 = 0
rus_2019 = 0
chi_2019 = 0
jap_2019 = 0
ind_2019 = 0
nk_2019 = 0

for (index, colname) in enumerate(df):
    if colname == "2019":
        avg_this_year = (df[colname].mean()) / 1000
        world_avg = (avg_this_year)
        usa_2019 = (usa.iloc[0][colname] / 1000)
        it_2019 = (it.iloc[0][colname] / 1000)
        uk_2019 = (uk.iloc[0][colname] / 1000)
        ger_2019 = (ger.iloc[0][colname] / 1000)
        fra_2019 = (fra.iloc[0][colname] / 1000)
        rus_2019 = (rus.iloc[0][colname] / 1000)
        chi_2019 = (chi.iloc[0][colname] / 1000)
        jap_2019 = (jap.iloc[0][colname] / 1000)
        ind_2019 = (ind.iloc[0][colname] / 1000)
        nk_2019 = (nk.iloc[0][colname] / 1000)


labels = ["Regno Unito", "Germania", "Giappone", "Francia", "Italia", "Media mondiale", "Stati Uniti", "Russia", "Corea del Nord", "Cina", "India"]
values_lower = [uk_2019, ger_2019, jap_2019, fra_2019, it_2019]
values_upper = [usa_2019, rus_2019, nk_2019, chi_2019, ind_2019]
width = 0.5
x = np.arange(len(labels))
ax.bar(x[0:5], values_lower, width,label = "Paesi con personale inferiore alla media", color = '#93E1F7')
ax.bar(x[5], world_avg, width, color = '#EC190B', label = "Media mondiale")
ax.bar(x[6:11], values_upper, width,label = "Paesi con personale superiore alla media", color = '#FFCD00')
ax.set_xticks(x, labels, fontsize = 7)

plt.show()
