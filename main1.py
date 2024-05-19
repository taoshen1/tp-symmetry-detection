import gudhi as gd
import gudhi.wasserstein
import warnings
from datetime import datetime
import numpy as np

# 获取当前时间
def main(image,slopes,nums):                            ###此处的nums指我需要上下移动多少次，例如3，就是在中心点及其上下移动一次
    start_time = datetime.now()            ###记录代码开始的时间
    height,width = image.shape
    center_x = image.shape[1] // 2  
    center_y= image.shape[0] // 2          ##得到中心点
    result = np.zeros_like(image)
    result1=np.zeros_like(image)    
    scores_dict2 = {}                      ###方便后续储存计算得到的L2-wasserstrin距离值的大小
    
    for j in slopes:                        ##控制斜率
        for i  in range(nums):              ##控制一个角度上下移动的条数
            for y in range(height):
                for x in range(width):
                    if y-(center_y)<j*(x-(center_x))+(-1) ** i * i // 2: 
                        result[y][x]=image[y][x]
                    else:
                        result1[y][x]=image[y][x]###为黑图进行重新描图
            cubical_complex_left = gd.CubicalComplex(dimensions=result.shape, top_dimensional_cells=result.flatten())
            cubical_complex_right = gd.CubicalComplex(dimensions=result1.shape, top_dimensional_cells=result1.flatten())
            a=cubical_complex_left.persistence()
            b=cubical_complex_right.persistence()
                    # 初始化两个空列表来存储分类后的数据点  
            left_class_0_data = []  
            left_class_1_data = []
            right_class_0_data = []  
            right_class_1_data = []  
              
            # 遍历原始数据，根据元组的第一个元素分类  
            for label, point in a:  
                if label == 0:  
                    left_class_0_data.append(list(point) + [label])  
                elif label == 1:  
                    left_class_1_data.append(list(point) + [label])
            for label, point in b:  
                if label == 0:  
                    right_class_0_data.append(list(point) + [label])  
                elif label == 1:  
                    right_class_1_data.append(list(point) + [label])####这部分主要是为了变一个形式进行计算
            right_1=np.array(right_class_1_data)
            right_0=np.array(right_class_0_data)
            left_1=np.array(left_class_1_data)
            left_0=np.array(left_class_0_data)
            score0=gd.wasserstein.wasserstein_distance(right_0,left_0,internal_p=2)
            score1=gd.wasserstein.wasserstein_distance(right_1,left_1,internal_p=2)
            score=score0+score1       
            scores_dict2[((-1) ** i * i // 2, j)] = score  
            result = np.zeros_like(image)
            result1=np.zeros_like(image)                          ###每次都需要初始化
      
    import pandas as pd  
    # 生成行索引序列  
    index_values = [(-1) ** i * i // 2 for i in range(nums)]  
      
    # 定义列索引列表 
    column_values = slopes
       
    # 创建 DataFrame，指定行索引和列索引  
    df2 = pd.DataFrame(index=index_values, columns=column_values)  
      
    for (i, j), score in scores_dict2.items():  
        df2.at[i, j] = score  
      
    # 打印 DataFrame  
    print(df2)
    end_time = datetime.now()
    
    # 计算时间差
    time_difference = end_time - start_time
    return df2
###函数的主要流程是：
###得到图像的大小和图像的中心点，并构建像素全为0的图像用于填图，其余部分保持黑色。
###分开计算0维和1维