import geopandas as gpd
from pyproj import Proj, transform
import matplotlib.pyplot as plt

# subzoneheat in the format of a dict {"MZ0123":200,"SH1001":100, ..}
def create_heat_map(subzoneheat):
    geodf = gpd.read_file("C:/Users/TKY/PycharmProjects/DataSpark/dataspark/flask_website/backend/stuff/MP14_SUBZONE_WEB_PL.shp")
    # legacy function if needed
    # initialize change of projections
    # inProj = Proj(init='epsg:3414')
    # outProj = Proj(init='epsg:4326')
    # geodf["temp"] = geodf.apply(lambda x: transform(inProj, outProj, x["X_ADDR"], x["Y_ADDR"]), axis=1)
    # geodf["x"] = geodf["temp"].loc[0][0]
    # geodf["y"] = geodf["temp"].loc[0][1]

    # add in the number of visitors to the subzone
    geodf["Visitors"] = geodf["SUBZONE_C"]
    geodf["Visitors"].replace(to_replace=subzoneheat, inplace=True)

    vmin, vmax = geodf['Visitors'].min(), geodf['Visitors'].max()
    ax = geodf.plot(column='Visitors', cmap='OrRd', vmin=vmin, vmax=vmax)
    plt.axis('off')
    fig = ax.get_figure()
    cax = fig.add_axes([0.9, 0.1, 0.03, 0.8])
    sm = plt.cm.ScalarMappable(cmap='OrRd', norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm._A = []
    plt.colorbar(sm, cax=cax)
    plt.savefig("heatmap.png")
    geodf.head()

