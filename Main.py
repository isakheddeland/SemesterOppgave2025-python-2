import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
from sklearn.metrics import r2_score

from data_handler import load_data, create_poly_model
from plotter import draw_the_map, draw_label_and_ticks
from utils import color_from_nedbor

df, X, ns = load_data()
model, poly, X_poly = create_poly_model(X, ns, degree=3)

marked_point = (0, 0)
current_view = 'month'


def update_graph(x, y, view='month'):
    if view == 'quarter':
        months_x = [1, 4, 7, 10]
    else:
        months_x = np.arange(1, 13)

    vectors = np.array([[x, y, m] for m in months_x])
    vectors_poly = poly.fit_transform(vectors)
    y_pred = model.predict(vectors_poly)
    aarsnedbor = sum(y_pred)

    axGraph.cla()
    draw_label_and_ticks(axGraph)
    axGraph.bar(months_x, y_pred, color=[color_from_nedbor(n*12) for n in y_pred])
    axGraph.plot(months_x, y_pred, color='black', linestyle='--', linewidth=2, label='Trend-linje')
    axGraph.axhline(y=np.mean(y_pred), color='red', linestyle='-', linewidth=2, label='Gj.snitt')
    axGraph.set_ylabel("mm")
    axGraph.grid(True, linestyle=':')
    axGraph.legend()
    axGraph.set_title(f"Nedbør per {'måned' if view=='month' else 'kvartal'}, Årsnedbør {int(aarsnedbor)} mm")
    plt.draw()


    std = np.std(y_pred)
    r2 = r2_score(ns, model.predict(X_poly))
    print(f"Standardavvik: {std:.2f}, R²: {r2:.2f}")

def on_click(event):
    global marked_point
    if event.inaxes != axMap: return

    marked_point = (event.xdata, event.ydata)
    axMap.scatter(marked_point[0], marked_point[1], c='red', s=350, marker='o')
    plt.draw()

    update_graph(*marked_point, view=current_view)

def on_radio(label):
    global current_view
    current_view = 'month' if label=='Måned' else 'quarter'
    if marked_point != (0,0):
        update_graph(*marked_point, view=current_view)


fig = plt.figure(figsize=(10, 4))
axGraph = fig.add_axes((0.05, 0.07, 0.35, 0.85))
axMap = fig.add_axes((0.41, 0.07, 0.59, 0.85))

draw_label_and_ticks(axGraph)
draw_the_map(axMap, df)


axRadio = fig.add_axes([0.02, 0.4, 0.1, 0.15])
radio = RadioButtons(axRadio, ('Måned', 'Kvartal'))
radio.on_clicked(on_radio)

plt.connect('button_press_event', on_click)
plt.show()


