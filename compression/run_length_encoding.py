import numpy as np

class Rle:
    def __init__(self):
        pass

    def encode_image(self, binary_image):
        """
        For efficiency, flatten the image by concatinating rows to create long array.
        Compute run length encoding on the long array.
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """

        row = len(binary_image)
        col = len(binary_image[0])
        flag = binary_image[0][0]
        count = 0
        rle_code = []

        if flag == 0:
            rle_code.append(0)
        else:
            rle_code.append(1)

        for i in range(0, row):
            for j in range(0, col):
                if binary_image[i][j] == flag:
                    count += 1
                else:
                    rle_code.append(count)
                    count = 1
                    if flag == 0:
                        flag = 255
                    else:
                        flag = 0

        return rle_code  # replace zeros with rle_code

    def decode_image(self, rle_code, height , width):
        """
        Since the image was flattened during the encoding, use the hight and width to reconstruct the image
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """

        image = np.zeros((height, width), np.uint8)
        color = 0
        row = 0
        col = 0

        if rle_code[0] == 1:
            color = 255

        for m in range(1, len(rle_code)):
            for n in range(0, rle_code[m]):
                image[row][col] = color
                col += 1
                if col >= width:
                    row += 1
                    col = 0
            if color == 0:
                color = 255
            else:
                color = 0

        return image  # replace zeros with image reconstructed from rle_Code





        




