import numpy as np
def  find_best(df):
    
    #######找行名和列名，也就是k和i
    values = df.values    
    # 找到最小值的扁平索引  
    flat_min_index = np.argmin(values)    
    # 将扁平索引转换为行索引和列索引  
    row_name = df.index[flat_min_index // df.shape[1]]  
    col_name = df.columns[flat_min_index % df.shape[1]]    
    # 获取最小值  
    min_value = df.at[row_name, col_name]    
    print(f"最小值：{min_value}")  
    print(f"行名：{row_name}")  
    print(f"列名：{col_name}")