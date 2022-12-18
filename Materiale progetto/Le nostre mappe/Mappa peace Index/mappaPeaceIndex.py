import geopandas as gdp
import contextily as ctx
import matplotlib.pyplot as plt
import pandas as pd
from shapely import wkt

gdf = gdp.read_file("earthFile.csv")
expenditures = pd.read_csv("peaceindex.csv")

gdf['geometry1'] = gdf['geometry1'].apply(wkt.loads) 
gdf.set_geometry('geometry1')


gdf = gdf.drop('geometry',axis = 1)
#gdf.rename_geometry('geometry',inplace = True)
gdf.rename(columns={'geometry1':'geometry'}, inplace=True)

nameSerieGDF = gdf['name']
nameSerieEXPENDITURES = expenditures['Country'].values

gdf['peaceindex'] = 0

x = range(177)

for i in x:
	if nameSerieGDF[i] in nameSerieEXPENDITURES:
		j = expenditures[expenditures['Country']== nameSerieGDF[i]].index.values.astype(int)[0]
		gdf.at[i,'peaceindex'] = expenditures.at[j,'2020']

# Convert to geopandas
realgdf = gdp.GeoDataFrame(gdf)

ax = realgdf.plot(column = 'peaceindex', missing_kwds={'color': 'lightgrey'}, legend = True,cmap = "Reds",legend_kwds={'label': "Peace index",'orientation': "horizontal"})
#ax.xaxis.label.set_color("#004249")
#ax.set_facecolor("#fac86a")
ax.set_axis_off();
#plt.savefig("1.png",bbox_inches='tight')
plt.show()