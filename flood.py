# import numpy as np
# import matplotlib.pyplot as plt
# from skimage import data, filters, color, morphology
# from skimage.segmentation import flood, flood_fill


# checkers = data.checkerboard()

# # Fill a square near the middle with value 127, starting at index (76, 76)
# filled_checkers = flood_fill(checkers, (76, 76), 127)

# fig, ax = plt.subplots(ncols=2, figsize=(10, 5))

# ax[0].imshow(checkers, cmap=plt.cm.gray)
# ax[0].set_title('Original')

# ax[1].imshow(filled_checkers, cmap=plt.cm.gray)
# ax[1].plot(76, 76, 'wo')  # seed point
# ax[1].set_title('After flood fill')

# plt.show()



# we need a 2D array to practice on
field = [
    [0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,1,1,0,0,0,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,1,1,0],
]

def print_field():
    # this function will print the content of the array to the console
    for y in range(len(field)):
        for x in range(len(field[0])):
            # value by column and row
            print(field[y][x], end=' ')
            if x == len(field[0])-1:
                # print a new line at the end of each row
                print('\n')

def flood_fill(x ,y, old, new):
    # we need the x and y of the start position, the old value,
    # and the new value

    # the flood fill has 4 parts

    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(field[0]) or y < 0 or y >= len(field):
        return

    # secondly, check if the current position equals the old value
    if field[y][x] != old:
        return

    # thirdly, set the current position to the new value
    field[y][x] = new

    # fourthly, attempt to fill the neighboring positions
    flood_fill(x+1, y, old, new)
    flood_fill(x-1, y, old, new)
    flood_fill(x, y+1, old, new)
    flood_fill(x, y-1, old, new)


if __name__ == "__main__":
    # print field before the flood fill
    print_field()

    flood_fill(0, 0, 0, 3)

    print("Doing flood fill with '3'")

    #print the field after the flood fill
    print_field()
