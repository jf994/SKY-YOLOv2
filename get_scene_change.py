import cv2
import numpy as np

def count_distance(old_ratio,new_ratio):

    i = 0
    val = 0
    for ratio in old_ratio:
        if (ratio + new_ratio[i] != 0):
            val += ((ratio - new_ratio[i]) ** 2)/(ratio + new_ratio[i])
        i += 1

    val *= 2
    new_ratio.append(val)
    return new_ratio

def count_nonblack_np(img):
    """Return the number of pixels in img that are not black.
    img must be a Numpy array with colour values along the last axis.

    """
    return img.any(axis=-1).sum()
def is_new_scene(image,old_ratio):
    red_ratio = 0
    blue_ratio = 0
    green_ratio = 0
    # define the list of boundaries
    boundaries = [
        ([17, 15, 100], [50, 56, 200]),  # red
        ([86, 31, 4], [220, 88, 50]), #blue
        ([35, 58, 0], [86, 255, 142]) #green
    ]
    i = 0
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        tot_pix = count_nonblack_np(image)
        color_pix = count_nonblack_np(output)
        ratio = color_pix / tot_pix
        # print("ratio is:", ratio)
        if i == 0:
            red_ratio = ratio
        elif i == 1:
            blue_ratio = ratio
        elif i == 2:
            green_ratio = ratio

        i += 1


    return count_distance(old_ratio,new_ratio=[red_ratio,blue_ratio,green_ratio])
