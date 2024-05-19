import math  
def angles_to_slopes(average_angles):  
    slopes = []  
    for angle in average_angles:  
        # 将角度转换为弧度  
        radian = math.radians(angle)  
        # 计算斜率（正切值）  
        # 注意：当 angle 接近 90 度时，tan 的值可能会非常大或溢出  
        # 在这种情况下，您可能需要处理这种情况以避免数值错误  
        try:  
            slope = math.tan(radian)  
        except ValueError:  
            # 当 angle 接近 90 度时，正切值可能无法计算  
            # 您可以设置 slope 为一个非常大的数或 'inf'  
            slope = float('inf')  
        slopes.append(slope)  
    return slopes   
