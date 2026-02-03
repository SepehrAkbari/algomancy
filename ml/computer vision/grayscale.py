'''
RGB to Grayscale Conversion.
'''

def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    weights = [0.299, 0.587, 0.114]
    
    for i in range(len(image)):
        for j in range(len(image[0])):
            colors = image[i][j]
            gray = float(weights[0] * colors[0] + weights[1] * colors[1] + weights[2] * colors[2])
            image[i][j] = gray
        
    return image
            

if __name__ == "__main__":
    image = [[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 255]]]
    print(color_to_grayscale(image))