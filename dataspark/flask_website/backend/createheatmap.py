import geopandas as gpd
from pyproj import Proj, transform
import matplotlib.pyplot as plt

geodf = gpd.read_file("C:/Users/TKY/Desktop/MP14_SUBZONE_WEB_PL.shp")

tempx = geodf.loc[5]["X_ADDR"]
tempy = geodf.loc[5]["Y_ADDR"]
inProj = Proj(init='epsg:3414')
outProj = Proj(init='epsg:4326')


geodf["temp"] = geodf.apply(lambda x: transform(inProj,outProj,x["X_ADDR"],x["Y_ADDR"]), axis=1)
geodf["x"] = geodf["temp"].loc[0][0]
geodf["y"] = geodf["temp"].loc[0][1]

vmin,vmax = geodf['SUBZONE_NO'].min(), geodf['SUBZONE_NO'].max()
ax = geodf.plot(column='SUBZONE_NO', cmap='OrRd', vmin=vmin, vmax=vmax)
plt.axis('off')
fig = ax.get_figure()
cax = fig.add_axes([0.9,0.1,0.03,0.8])
sm = plt.cm.ScalarMappable(cmap = 'OrRd',norm= plt.Normalize(vmin=vmin,vmax=vmax))
sm._A = []
plt.colorbar(sm,cax=cax)
plt.savefig("heatmap.png")
