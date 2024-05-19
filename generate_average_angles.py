##和角度转斜率一起使用，把产生的角度变为斜率进行后续计算
def generate_average_angles(total_degrees, n):  
    step = total_degrees / n  # 计算每个步骤的度数  
    angles = [i * step for i in range(n)]  # 生成包含n+1个元素的序列，包括0度和total_degrees  
    return angles  
if __name__=="__main__" :
    
  # 输入份数，比如10  
    average_angles = generate_average_angles(180, int(input('请输入平均分的份数: ')))  
    print(average_angles)