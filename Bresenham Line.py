
import matplotlib.pyplot as plt

def plot_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    steep = dy > dx

    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dy = abs(y1 - y0)
    err = 0
    y = y0
    ystep = 1 if y0 < y1 else -1

    points = []
    for x in range(x0, x1 + 1):
        coord = (y, x) if steep else (x, y)
        points.append(coord)
        err += dy
        if 2 * err >= dx:
            y += ystep
            err -= dx

    return points

# Example usage:

x0, y0 = 1, 1
x1, y1 = 15, 5

line_points = plot_line(x0, y0, x1, y1)

# Plotting the line
plt.plot(*zip(*line_points), marker='o')
plt.show()
