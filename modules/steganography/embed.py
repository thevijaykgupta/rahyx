import cv2
from utils.converter import text_to_binary

def embed_data(image_path, data, output_path):
    img = cv2.imread(image_path)
    binary_data = text_to_binary(data) + '1111111111111110'  # delimiter

    data_index = 0
    for row in img:
        for pixel in row:
            for i in range(3):  # RGB
                if data_index < len(binary_data):
                    pixel[i] = pixel[i] & 254 | int(binary_data[data_index])
                    data_index += 1

    cv2.imwrite(output_path, img)