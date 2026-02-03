'''
Intersection over Union (IoU).
'''

def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    if len(box_a) != 4 or len(box_b) != 4:
        raise ValueError
    
    x_left = max(box_a[0], box_b[0])
    y_top = max(box_a[1], box_b[1])
    x_right = min(box_a[2], box_b[2])
    y_bottom = min(box_a[3], box_b[3])
    
    if x_right < x_left or y_bottom < y_top:
        return 0.0
    
    a_area = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    b_area = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
    
    intersection_area = (x_right - x_left) * (y_bottom - y_top)
    union_area = a_area + b_area - intersection_area
    
    return intersection_area / union_area
    
    
if __name__ == "__main__":
    box_a = [0, 0, 4, 4] 
    box_b = [2, 2, 6, 6]
    print(iou(box_a, box_b))