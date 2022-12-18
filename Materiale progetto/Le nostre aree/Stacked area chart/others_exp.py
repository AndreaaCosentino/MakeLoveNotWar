import pandas as pd

START_COL = 24 # 1980 
END_COL = 65

csv = pd.read_csv("API_MS.MIL.XPND.CD_DS2_en_csv_v2_4694395.csv")

others_exp = csv[csv["Country Name"] != "France"]
others_exp = others_exp[csv["Country Name"] != "Italy"]
others_exp = others_exp[csv["Country Name"] != "Germany"]
others_exp = others_exp[csv["Country Name"] != "United Kingdom"]
others_exp = others_exp[csv["Country Name"] != "United States"]
others_exp = others_exp.iloc[:, START_COL:END_COL]

others_exp = others_exp.dropna()
others_exp_values = others_exp.values[0]
