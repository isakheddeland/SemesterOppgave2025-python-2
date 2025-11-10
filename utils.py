colors = ['orange', 'gray', 'blue', 'darkblue', 'black']
legend_mm = [0, 1300, 1700, 2500, 3200]

def index_from_nedbor(x):
    if x < 1300: return 0
    if x < 1700: return 1
    if x < 2500: return 2
    if x < 3200: return 3
    return 4

def color_from_nedbor(nedbor):
    from utils import colors
    return colors[index_from_nedbor(nedbor)]

def size_from_nedbor(nedbor):
    return 350

def label_from_nedbor(nedbor):
    return str(int(nedbor / 100))
