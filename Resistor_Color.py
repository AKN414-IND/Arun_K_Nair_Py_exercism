def color_code(color):
    colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    color_to_value = dict(zip(colors, values))
    
    return color_to_value.get(color.lower(), None)

def colors():
    colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return colors
