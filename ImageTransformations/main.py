from utils import *
import numpy as np

def grayScaledFilter(img):
    
    grey_filter= np.array([[0.33,0.33,0.33],[0.33,0.33,0.33],[0.33,0.33,0.33]])
    grey_pic = Filter(img, grey_filter)
    return grey_pic

def customFilter(img):
   
    my_filter = np.array([[1,4,0],[0,1,3],[2,7,2]])
    my_pic = Filter(img, my_filter)
    showImage(my_pic, title="@_@")

    my_filter_inv = np.linalg.inv(my_filter)
    my_pic_inv = Filter(my_pic, my_filter_inv)
    showImage(my_pic_inv, title="^_^")


def scaleImg(img, scale_width, scale_height):
   
    new_width = img.shape[1] * scale_width
    new_height = img.shape[0] * scale_height
    scaled_img = np.zeros(( new_height,new_width, 3))
    for h in range(new_height):
        h_in_first_image = int(h / scale_height)
        for  w in range(new_width):
            w_in_first_image = int(w / scale_width)
            pixel_value = img[h_in_first_image,w_in_first_image,:]
            scaled_img[h, w, :] = pixel_value
    return scaled_img
    


def cropImg(img, start_row, end_row, start_column, end_column):  #50, 300, 50, 225
   
    new_row_num = end_row-start_row
    new_column_num = end_column-start_column
    cropped_image = np.zeros((new_row_num,new_column_num,img.shape[2]))

    for r in range(new_row_num):
        r_in_original_image = r+start_row
        for c in range(new_column_num):
            c_in_original_image = c+start_column
            cropped_image[r][c] = img[r_in_original_image][c_in_original_image]
    return cropped_image

if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')
 

    showImage(image_matrix, title="Input Image")

    grayScalePic = grayScaledFilter(image_matrix)
    showImage(grayScalePic, title="Gray Scaled")

    customFilter(image_matrix)

    croppedImage = cropImg(image_matrix, 50, 300, 50, 225)
    showImage(croppedImage, title="Cropped Image")

    scaledImage = scaleImg(image_matrix, 2, 3)
    showImage(scaledImage, title="Scaled Image")
