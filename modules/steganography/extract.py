import cv2

def extract_data(image_path):
    img = cv2.imread(image_path)
    binary_data = ""

    for row in img:
        for pixel in row:
            for i in range(3):
                binary_data += str(pixel[i] & 1)

    # split using delimiter
    end_marker = "1111111111111110"
    data = binary_data.split(end_marker)[0]

    # convert binary to text
    chars = [data[i:i+8] for i in range(0, len(data), 8)]
    message = ''.join([chr(int(c, 2)) for c in chars])

    return message