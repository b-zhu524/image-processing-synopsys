import cv2
import numpy as np
"""
objectives

1 -- find the difference in color (plot on a graph as a scatter plot)

2 -- find the overall whiteness before and after (plot this on the same graph)
"""


def main():
    tests_total = 1 # size of dataset

    img = f"white.jpg"
    avg_color = average_color(img)  # average vector [R, G, B]
    avg_int = sum(avg_color) / 3    # average of R, G, B
    return 255 - avg_int    # smaller number means whiter image


def average_color(img):
    image = cv2.imread(img)
    average_color_row = np.average(image, axis=0)
    _average_color = np.average(average_color_row, axis=0)
    return _average_color


if __name__ == "__main__":
    print(main())
