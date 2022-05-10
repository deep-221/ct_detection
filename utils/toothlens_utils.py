# Here are all the utility functions needed to cater toothlens product

def yolo_to_nrml_coordinates(img_shape_list, yolo_coordinates_list):
    """
    This function converts yolo coordinates of bbox to normal pixel coordinates

    :param img_shape_list: list of [height, width] of the image to find bbox coordinates for
        :param yolo_coordinates_list: list of [x, y, w, h] directly taken from each line of annotation txt
    :return: list of [x_min, y_min, x_max, y_max] in normal coordinate system to draw rectangle
    """
    #import cv2
    dw = img_shape_list[1]
    dh = img_shape_list[0]
    coordinates_list = []

    #path_to_img = "C:/Users/mehta/Desktop/Desktop/Fiverr/Manoj/dataset/detection/original/train_images/1001_1500/1457_lj_ct.jpg"
    #img = cv2.imread(path_to_img)

    for bbox_count in yolo_coordinates_list:
        x, y, w, h = bbox_count
        x_min = int((x - w / 2) * dw)
        x_max = int((x + w / 2) * dw)
        y_min = int((y - h / 2) * dh)
        y_max = int((y + h / 2) * dh)

        if x_min < 0:
            x_min = 0
        if x_max > dw - 1:
            x_max = dw - 1
        if y_min < 0:
            y_min = 0
        if y_max > dh - 1:
            y_max = dh - 1

        # cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 0, 255), 1)
        coordinates_list.append([x_min, y_min, x_max, y_max])

    #cv2.imshow("image_with_bbox", img)
    #cv2.waitKey(0)

    return coordinates_list