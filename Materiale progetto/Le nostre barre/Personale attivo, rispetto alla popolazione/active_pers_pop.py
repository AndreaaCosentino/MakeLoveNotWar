import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("API_MS.MIL.TOTL.P1_DS2_en_csv_v2_4689881.csv")
pop_df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_4759907.csv")

fig, ax = plt.subplots()

fig.set_size_inches(11,7)

#plt.suptitle("Numero personale militare in base alla popolazione (Anno 2019)", fontsize = 20)

all_years = []

usa = df[df['Country Name'] == "United States"]
usa_pop = pop_df[pop_df['Country Name'] == "United States"]
it = df[df['Country Name'] == "Italy"]
it_pop = pop_df[pop_df['Country Name'] == "Italy"]
uk = df[df['Country Name'] == "United Kingdom"]
uk_pop = pop_df[pop_df['Country Name'] == "United Kingdom"]
ger = df[df['Country Name'] == "Germany"]
ger_pop = pop_df[pop_df['Country Name'] == "Germany"]
fra = df[df['Country Name'] == "France"]
fra_pop = pop_df[pop_df['Country Name'] == "France"]
rus = df[df['Country Name'] == "Russian Federation"]
rus_pop = pop_df[pop_df['Country Name'] == "Russian Federation"]
chi = df[df['Country Name'] == "China"]
chi_pop = pop_df[pop_df['Country Name'] == "China"]
jap = df[df['Country Name'] == "Japan"]
jap_pop = pop_df[pop_df['Country Name'] == "Japan"]
ind = df[df['Country Name'] == "India"]
ind_pop = pop_df[pop_df['Country Name'] == "India"]
nk = df[df['Country Name'] == "Korea, Dem. People's Rep."]
nk_pop = pop_df[pop_df['Country Name'] == "Korea, Dem. People's Rep."]

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
        avg_this_year = (df[colname].mean())
        pop = pop_df[colname].mean()
        world_avg = (avg_this_year / pop)*100
        usa_2019 = (usa.iloc[0][colname] / usa_pop.iloc[0][colname]*100)
        it_2019 = (it.iloc[0][colname] / it_pop.iloc[0][colname]*100)
        uk_2019 = (uk.iloc[0][colname] / uk_pop.iloc[0][colname]*100)
        ger_2019 = (ger.iloc[0][colname] / ger_pop.iloc[0][colname]*100)
        fra_2019 = (fra.iloc[0][colname] / fra_pop.iloc[0][colname]*100)
        rus_2019 = (rus.iloc[0][colname] / rus_pop.iloc[0][colname]*100)
        chi_2019 = (chi.iloc[0][colname] / chi_pop.iloc[0][colname]*100)
        jap_2019 = (jap.iloc[0][colname] / jap_pop.iloc[0][colname]*100)
        ind_2019 = (ind.iloc[0][colname] / ind_pop.iloc[0][colname]*100)
        nk_2019 = (nk.iloc[0][colname] / nk_pop.iloc[0][colname]*100)


labels = ["Cina", "Giappone", "Germania", "India", "Regno Unito", "Media mondiale", "Stati Uniti", "Francia", "Italia", "Russia", "Corea del Nord"]
values_lower = [chi_2019, jap_2019, ger_2019, ind_2019, uk_2019]
values_upper = [usa_2019, fra_2019, it_2019, rus_2019, nk_2019]
width = 0.5
x = np.arange(len(labels))
ax.bar(x[0:5], values_lower, width,label = "Paesi con personale inferiore alla media", color = '#93E1F7')
ax.bar(x[5], world_avg, width, color = '#EC190B', label = "Media mondiale")
ax.bar(x[6:11], values_upper, width,label = "Paesi con personale superiore alla media", color = '#FFCD00')
ax.set_xticks(x, labels, fontsize = 7)
ax.set_yticks(ticks =[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6])

plt.show()
