import cv2
import numpy as np
import math


class CellCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 5 pixel cross window assigns region names
        takes a input:
        image: binary image
        return: a list of regions"""

        regions = dict()
        row = len(image)
        col = len(image[0])
        r = np.zeros((row, col))
        k = 1
        count = 1
        array = []

        for i in range(0, row):
            for j in range(0, col):
                if (i == 0) and (j == 0):
                    if image[i][j] == 255:
                        r[i][j] = k
                        k += 1
                elif i == 0:
                    if image[i][j] == 255 and image[i][j - 1] == 0:
                        r[i][j] = k
                        k += 1
                    if image[i][j] == 255 and image[i][j - 1] == 255:
                        r[i][j] = r[i][j - 1]
                elif j == 0:
                    if image[i][j] == 255 and image[i - 1][j] == 0:
                        r[i][j] = k
                        k += 1
                    if image[i][j] == 255 and image[i - 1][j] == 255:
                        r[i][j] = r[i - 1][j]
                else:
                    if image[i][j] == 255 and image[i][j - 1] == 0 and image[i - 1][j] == 0:
                        r[i][j] = k
                        k += 1
                    if image[i][j] == 255 and image[i][j - 1] == 0 and image[i - 1][j] == 255:
                        r[i][j] = r[i - 1][j]
                    if image[i][j] == 255 and image[i][j - 1] == 255 and image[i - 1][j] == 0:
                        r[i][j] = r[i][j - 1]
                    if image[i][j] == 255 and image[i][j - 1] == 255 and image[i - 1][j] == 255:
                        r[i][j] = r[i - 1][j]
                        if r[i][j - 1] != r[i][j]:
                            r[i][j - 1] = r[i][j]

        for i in range(0, row-1):
            for j in range(0, col-1):
                if r[i][j] == 0:
                    continue
                if (r[i][j] != r[i][j + 1]) and (r[i][j+1] != 0):
                    temp = r[i][j]
                    rep = r[i][j+1]
                    for m in range(0, row):
                        for n in range(0, col):
                            if r[m][n] == rep:
                                r[m][n] = temp

        for i in range(1, row-1):
            for j in range(1, col-1):
                if (r[i][j] in array) or (r[i][j] == 0):
                    continue
                else:
                    count_area = 0
                    array.append(r[i][j])
                    k = r[i][j]
                    sum_x = 0
                    sum_y = 0
                    for m in range(0, row):
                        for n in range(0, col):
                            if r[m][n] == k:
                                count_area += 1
                                sum_x += m
                                sum_y += n
                    regions[count] = ((round(sum_x/count_area), round(sum_y/count_area)), count_area)
                    count += 1

        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: list regions and corresponding pixels
        returns: stats"""

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        stats = region
        print(stats)

        return stats

    def mark_image_regions(self, image, stats):
        """Creates a new image with computed stats
        Make a copy of the image on which you can write text. 
        takes as input
        image: Input binary image
        stats: stats regarding location and area
        returns: image marked with center and area"""

        mark_img = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        for i in stats:
            if stats[i][1] >= 15:
                cv2.putText(mark_img, "*", (stats[i][0][1]-4, stats[i][0][0]+4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, 16)
                cv2.putText(mark_img, " " + str(i) + "," + str(stats[i][1]), (stats[i][0][1], stats[i][0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 255), 1, -1)

        return mark_img

