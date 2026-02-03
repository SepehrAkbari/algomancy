'''
Image Histogram.
'''

def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    hist = [0] * 256

    for i in range(len(image)):
        for j in range(len(image[0])):
            hist[image[i][j]] += 1
    
    return hist
    
    
if __name__ == "__main__":
    image = [[128, 128], [128, 255]]
    print(image_histogram(image))