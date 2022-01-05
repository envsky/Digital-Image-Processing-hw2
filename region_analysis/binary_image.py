import math

class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""

        row = len(image)
        col = len(image[0])

        hist = [0] * 256

        for i in range(0, row):
            for j in range(0, col):
                hist[image[i][j]] += 1

        return hist

    def find_otsu_threshold(self, hist):
        """analyses a histogram to find the otsu's threshold assuming that the input histogram is bimodal.
        takes as input
        hist: a histogram
        returns: an optimal threshold value (otsu's threshold)"""

        total, sum_b, sum_f, weight_b, weight_f, mean_b, mean_f = 0, 0, 0, 0, 0, 0, 0
        var_b, var_f, within_class_var, minimum, threshold = 0, 0, 0, 0, 0

        for i in range(0, len(hist)):
            total = total + hist[i]

        for t in range(0, len(hist)):

            for i in range(0, t):
                weight_b = weight_b + hist[i]
                mean_b = mean_b + (i * hist[i])
            sum_b = weight_b
            weight_b = weight_b / total
            if sum_b == 0:
                mean_b = 0
            else:
                mean_b = mean_b / sum_b

            for i in range(0, t):
                var_b = var_b + ((i - mean_b) * (i - mean_b)) * hist[i]
            if sum_b == 0:
                var_b = 0
            else:
                var_b = var_b / sum_b

            for i in range(t, len(hist)):
                weight_f = weight_f + hist[i]
                mean_f = mean_f + (i * hist[i])
            sum_f = weight_f
            weight_f = weight_f / total
            if sum_f == 0:
                mean_f = 0
            else:
                mean_f = mean_f / sum_f

            for i in range(t, len(hist)):
                var_f = var_f + ((i - mean_f) * (i - mean_f)) * hist[i]
            if sum_f == 0:
                var_f = 0
            else:
                var_f = var_f / sum_f

            within_class_var = (weight_b * var_b) + (weight_f * var_f)

            if (within_class_var < minimum) or (t == 0):
                minimum = within_class_var
                threshold = t

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        Make calls to the compute_histogram and find_otsu_threshold methods as needed.
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()

        row = len(bin_img)
        col = len(bin_img[0])

        threshold = self.find_otsu_threshold(self.compute_histogram(image))

        for i in range(0, row):
            for j in range(0, col):
                if bin_img[i][j] <= threshold:
                    bin_img[i][j] = 255
                else:
                    bin_img[i][j] = 0

        return bin_img
