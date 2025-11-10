import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from utils import color_from_nedbor, size_from_nedbor, label_from_nedbor, colors, legend_mm

def draw_label_and_ticks(axGraph):
    xlabels = ['J','F','M','A','M','J','J','A','S','O','N','D']
    axGraph.set_xticks(range(1,13))
    axGraph.set_xticklabels(xlabels)

def draw_legend(axMap):
    for i, col in enumerate(colors):
        axMap.scatter([], [], c=col, s=200, label=f"{legend_mm[i]} mm")
    axMap.legend(loc='upper left', title="Nedbør", fontsize=10)

def draw_the_map(axMap, df):
    axMap.cla()
    img = mpimg.imread('images/StorBergen2.png')
    axMap.imshow(img, extent=(0, 13, 0, 10))
    axMap.set_xlim(0, 13)
    axMap.set_ylim(0, 10)

    df_year = df.groupby(['X','Y']).agg({'Nedbor':'sum'}).reset_index()
    xr = df_year['X'].tolist()
    yr = df_year['Y'].tolist()
    nedborAar = df_year['Nedbor']

    ColorList = [color_from_nedbor(n) for n in nedborAar]
    axMap.scatter(xr, yr, c=ColorList, s=size_from_nedbor(nedborAar/12), alpha=1)

    for i in range(len(xr)):
        axMap.text(xr[i], yr[i], s=label_from_nedbor(nedborAar[i]), color='white', fontsize=10, ha='center', va='center')
    draw_legend(axMap)
    axMap.set_title("click rød er estimert")
    axMap.axis('off')
    axMap.margins(x=0.01, y=0.01)
