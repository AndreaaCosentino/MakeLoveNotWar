import numpy as np
import pandas as pd
from others_exp import others_exp_values

START_COL = 24 # 1980 
END_COL = 65

csv = pd.read_csv("API_MS.MIL.XPND.CD_DS2_en_csv_v2_4694395.csv")

france_exp = csv[csv["Country Name"] == "France"]
france_exp = france_exp.iloc[:, START_COL:END_COL]
italy_exp = csv[csv["Country Name"] == "Italy"]
italy_exp = italy_exp.iloc[:, START_COL:END_COL]
germany_exp = csv[csv["Country Name"] == "Germany"]
germany_exp = germany_exp.iloc[:, START_COL:END_COL]
uk_exp = csv[csv["Country Name"] == "United Kingdom"]
uk_exp = uk_exp.iloc[:, START_COL:END_COL]
usa_exp = csv[csv["Country Name"] == "United States"]
usa_exp = usa_exp.iloc[:, START_COL:END_COL]

france_exp_values = france_exp.values[0]
italy_exp_values = italy_exp.values[0]
germany_exp_values = germany_exp.values[0]
uk_exp_values = uk_exp.values[0]
usa_exp_values = usa_exp.values[0]

exp_values = np.array([others_exp_values, germany_exp_values, france_exp_values, italy_exp_values, uk_exp_values, usa_exp_values], dtype=float)