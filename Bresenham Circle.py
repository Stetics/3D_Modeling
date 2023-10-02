import matplotlib.pyplot as plt
import numpy as np
def draw_circle(center_x, center_y, radius, image):
    x = radius
    y = 0
    radius_error = 1 - x
    while x >= y:
        plot_circle_points(center_x, center_y, x, y, image)
        y += 1
        if radius_error < 0:
            radius_error += 2 * y + 1
        else:
            x -= 1
            radius_error += 2 * (y - x + 1)
def plot_circle_points(center_x, center_y, x, y, image):
    points = [
        (x, y), (-x, y), (x, -y), (-x, -y),
        (y, x), (-y, x), (y, -x), (-y, -x)
    ]
    for point in points:
        pixel_x = center_x + point[0]
        pixel_y = center_y + point[1]
        if 0 <= pixel_x < image.shape[1] and 0 <= pixel_y < image.shape[0]:
            image[pixel_y, pixel_x] = 1
width = int(input("Введите ширину изображения: "))
height = int(input("Введите высоту изображения: "))
image = np.zeros((height, width), dtype=np.uint8)
center_x = int(input("Введите x координату центра окружности: "))
center_y = int(input("Введите y координату центра окружности: "))
radius = int(input("Введите радиус окружности: "))
draw_circle(center_x, center_y, radius, image)
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.show()