import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
objectives

1 -- find the difference in color (plot on a graph as a scatter plot)

2 -- find the overall whiteness before and after (plot this on the same graph)
"""


def main():
    tests_total = 1 # size of dataset

    trial_number = [int(i) for i in range(1, tests_total+1)]
    changeList = []
    whtBefore = []
    whtAfter = []

    for i in range(1, tests_total+1):
        img_before = f"{i}before.jpg"
        img_after = f"{i}after.jpg"

        # process the before image
        avg_color = average_color(img_before)  # average vector [R, G, B]
        whiteness_before = sum(avg_color) / 3    # larger number means whiter image
        whtBefore.append(whiteness_before)

        # process the after image
        avg_color_after = average_color(img_after)
        whiteness_after = sum(avg_color_after) / 3    # larger number means whiter image
        whtAfter.append(whiteness_after)

        change = whiteness_after - whiteness_before # larger value means more effect
        changeList.append(change)

        print(whiteness_before, whiteness_after, change)

    plotData(trial_number, whtBefore, whtAfter, changeList)


def average_color(img):
    image = cv2.imread(img)
    average_color_row = np.average(image, axis=0)
    _average_color = np.average(average_color_row, axis=0)
    return _average_color


def plotData(trial_number, avg_color_before, avg_color_after, change):
    plt.title("Measuring The Efficacy of a Whiteboard Cleaner")
    plt.xlabel("trial number")
    plt.ylabel("y-axis")
    plt.scatter(trial_number, avg_color_before, c="r")  # before = red

    plt.scatter(trial_number, avg_color_after, c="g")   # after = green

    plt.scatter(trial_number, change, c="b")    # change = blue

    plt.legend(["before", "after", "change"])
    plt.show()


if __name__ == "__main__":
    main()
